import datetime

from testing_runner import models
from testing_user import models as user_models
from testing_runner.utils.parser import Format
from djcelery import models as celery_models


def get_counter(model, pk=None):
    """
    统计相关表长度
    """
    if pk:
        return model.objects.filter(project__id=pk).count()
    else:
        return model.objects.count()


def get_day(d):
    """
    循环得到天数 7天
    """
    for i in range(1, 8):
        oneday = datetime.timedelta(days=i)
        day = d - oneday
        date_to = datetime.datetime(day.year, day.month, day.day)
        yield str(date_to)[0:10]


def get_recently_data(model):
    """
    得到报表数据
    """
    # 获取当前时间，计算当前日期往前推7天
    cur_time = datetime.datetime.now()
    day = get_day(cur_time)
    day_list = []
    for obj in day:
        day_list.append(obj)
    day_list = day_list[::-1]

    data_recently = []
    count = 0
    for day in day_list:
        recently_count = model.objects.filter(create_time__contains=day).count()
        detail = {'date': day, 'value': recently_count}
        data_recently.append(detail)
        count = count + recently_count

    return data_recently, count


def get_possess_detail():
    """
    首页详细统计信息
    """
    user_count = get_counter(user_models.UserInfo)
    update_time = datetime.datetime.now().date()
    token_count = user_models.UserToken.objects.filter(update_time__contains=update_time).count()
    project_count = get_counter(models.Project)
    report_count = get_counter(models.Report)
    case_count = get_counter(models.Case)
    mock_count = get_counter(models.Mock)
    task_count = celery_models.PeriodicTask.objects.filter().count()

    user_recently, user_recently_count = get_recently_data(user_models.UserInfo)
    project_recently, project_recently_count = get_recently_data(models.Project)
    case_recently, case_recently_count = get_recently_data(models.Case)
    mock_recently, mock_recently_count = get_recently_data(models.Mock)
    report_recently, report_recently_count = get_recently_data(models.Report)

    return {
        'user_count': user_count,
        'token_count': token_count,
        'project_count': project_count,
        'report_count': report_count,
        'case_count': case_count,
        'mock_count': mock_count,
        'task_count': task_count,
        'user_recently_count': user_recently_count,
        'user_recently': user_recently,
        'project_recently_count': project_recently_count,
        'project_recently': project_recently,
        'case_recently_count': case_recently_count,
        'case_recently': case_recently,
        'mock_recently_count': mock_recently_count,
        'mock_recently': mock_recently,
        'report_recently_count': report_recently_count,
        'report_recently': report_recently,
    }


def get_project_detail(pk):
    """
    项目详细统计信息
    """
    api_count = get_counter(models.API, pk=pk)
    case_count = get_counter(models.Case, pk=pk)
    config_count = get_counter(models.Config, pk=pk)
    variables_count = get_counter(models.Variables, pk=pk)
    report_count = get_counter(models.Report, pk=pk)
    host_count = get_counter(models.HostIP, pk=pk)
    mock_count = get_counter(models.Mock, pk=pk)
    task_count = celery_models.PeriodicTask.objects.filter(description=pk).count()

    return {
        'api_count': api_count,
        'case_count': case_count,
        'task_count': task_count,
        'config_count': config_count,
        'variables_count': variables_count,
        'report_count': report_count,
        'host_count': host_count,
        'mock_count': mock_count
    }


def project_init(project, username):
    """
    新建项目初始化
    """

    # 自动生成默认debugtalk.py
    models.Debugtalk.objects.create(project=project, creator=username)
    # 自动生成API tree
    models.Relation.objects.create(project=project)
    # 自动生成Test Tree
    models.Relation.objects.create(project=project, type=2)
    # 自动生成Mock Tree
    models.Relation.objects.create(project=project, type=3)


def project_end(project):
    """
    删除项目相关表 filter不会报异常 最好不用get
    """
    models.Debugtalk.objects.filter(project=project).delete()
    models.Config.objects.filter(project=project).delete()
    models.API.objects.filter(project=project).delete()
    models.Relation.objects.filter(project=project).delete()
    models.Report.objects.filter(project=project).delete()
    models.Variables.objects.filter(project=project).delete()
    celery_models.PeriodicTask.objects.filter(description=project).delete()

    case = models.Case.objects.filter(project=project).values_list('id')

    for case_id in case:
        models.CaseStep.objects.filter(case__id=case_id).delete()


def tree_end(params, project):
    """
    project: Project Model
    params: {
        node: int,
        type: int
    }
    """
    type = params['type']
    node = params['node']

    if type == 1:
        models.API.objects. \
            filter(relation=node, project=project).delete()

    # remove node testcase
    elif type == 2:
        case = models.Case.objects. \
            filter(relation=node, project=project).values('id')

        for case_id in case:
            models.CaseStep.objects.filter(case__id=case_id['id']).delete()
            models.Case.objects.filter(id=case_id['id']).delete()


def update_casestep(body, case, username):
    step_list = list(models.CaseStep.objects.filter(case=case).values('id'))

    for index in range(len(body)):

        test = body[index]
        try:
            format_http = Format(test['newBody'])
            format_http.parse()
            name = format_http.name
            new_body = format_http.testcase
            url = format_http.url
            method = format_http.method
            # 如果用例中API后续修改的话则设置source_api_id为0，避免同步时把修改的也同步
            source_api_id = 0
        except KeyError:
            if 'case' in test.keys():
                case_step = models.CaseStep.objects.get(id=test['id'])
            elif test['body']['method'] == 'config':
                case_step = models.Config.objects.get(name=test['body']['name'])
            else:
                case_step = models.API.objects.get(id=test['id'])

            new_body = eval(case_step.body)
            name = test['body']['name']

            if case_step.name != name:
                new_body['name'] = name

            if test['body']['method'] == 'config':
                url = ''
                method = 'config'
                # config没有source_api_id,默认为0
                source_api_id = 0
            else:
                url = test['body']['url']
                method = test['body']['method']
                source_api_id = test.get('source_api_id', 0)
                # 新增的case_step没有source_api_id字段,需要重新赋值
                if source_api_id == 0:
                    source_api_id = test['id']
        kwargs = {
            'name': name,
            'body': new_body,
            'url': url,
            'method': method,
            'step': index,
            "source_api_id": source_api_id
        }
        if 'case' in test.keys():
            models.CaseStep.objects.filter(id=test['id']).update(**kwargs, updater=username, update_time=datetime.datetime.now())
            step_list.remove({'id': test['id']})
        else:
            kwargs['case'] = case
            models.CaseStep.objects.create(**kwargs, creator=username)

    #  去掉多余的step
    for content in step_list:
        models.CaseStep.objects.filter(id=content['id']).delete()


def generate_casestep(body, case, username):
    """
    生成用例集步骤
    """
    #  index也是case step的执行顺序

    for index in range(len(body)):

        test = body[index]
        try:
            format_http = Format(test['newBody'])
            format_http.parse()
            name = format_http.name
            new_body = format_http.testcase
            url = format_http.url
            method = format_http.method
            # 如果用例中API后续修改的话则设置source_api_id为0，避免同步时把修改的也同步
            source_api_id = 0

        except KeyError:
            if test['body']['method'] == 'config':
                name = test['body']['name']
                method = test['body']['method']
                config = models.Config.objects.get(name=name)
                url = config.base_url
                new_body = eval(config.body)
                source_api_id = 0  # config没有api,默认为0
            else:
                api = models.API.objects.get(id=test['id'])
                new_body = eval(api.body)
                name = test['body']['name']

                if api.name != name:
                    new_body['name'] = name

                url = test['body']['url']
                method = test['body']['method']
                source_api_id = test['id']

        kwargs = {
            'name': name,
            'body': new_body,
            'url': url,
            'method': method,
            'step': index,
            'case': case,
            "source_api_id": source_api_id,
            "creator": username
        }

        models.CaseStep.objects.create(**kwargs)


def case_end(pk):
    """
    pk: int case id
    """
    models.CaseStep.objects.filter(case__id=pk).delete()
    models.Case.objects.filter(id=pk).delete()
