PROJECT_ADD_SUCCESS = {
    'code': '0001',
    'success': True,
    'msg': '项目添加成功'
}

PROJECT_EXISTS = {
    'code': '0101',
    'success': False,
    'msg': '项目已存在'
}

PROJECT_NOT_EXISTS = {
    'code': '0102',
    'success': False,
    'msg': '项目不存在'
}

DEBUGTALK_NOT_EXISTS = {
    'code': '0102',
    'success': False,
    'msg': 'miss debugtalk'
}

DEBUGTALK_UPDATE_SUCCESS = {
    'code': '0002',
    'success': True,
    'msg': 'debugtalk更新成功'
}

PROJECT_UPDATE_SUCCESS = {
    'code': '0002',
    'success': True,
    'msg': '项目更新成功'
}

PROJECT_DELETE_SUCCESS = {
    'code': '0003',
    'success': True,
    'msg': '项目删除成功'
}

SYSTEM_ERROR = {
    'code': '9999',
    'success': False,
    'msg': 'System Error'
}

TREE_ADD_SUCCESS = {
    'code': '0001',
    'success': True,
    'msg': '树形结构添加成功'
}

TREE_UPDATE_SUCCESS = {
    'code': '0002',
    'success': True,
    'msg': '树形结构更新成功'
}

KEY_MISS = {
    'code': '0100',
    'success': False,
    'msg': '请求数据非法'
}

FILE_UPLOAD_SUCCESS = {
    'code': '0001',
    'success': True,
    'msg': '文件上传成功'
}

FILE_EXISTS = {
    'code': '0101',
    'success': False,
    'msg': '文件已存在,默认使用已有文件'
}

API_ADD_SUCCESS = {
    'code': '0001',
    'success': True,
    'msg': '接口添加成功'
}

DATA_TO_LONG = {
    'code': '0100',
    'success': False,
    'msg': '数据信息过长！'
}

API_NOT_FOUND = {
    'code': '0102',
    'success': False,
    'msg': '未查询到该API'
}

API_DEL_SUCCESS = {
    'code': '0003',
    'success': True,
    'msg': 'API删除成功'
}

REPORT_DEL_SUCCESS = {
    'code': '0003',
    'success': True,
    'msg': '报告删除成功'
}

API_UPDATE_SUCCESS = {
    'code': '0002',
    'success': True,
    'msg': 'API更新成功'
}

API_UPDATE_EXISTS = {
    "code": "0002",
    "success": False,
    "msg": "接口状态更新失败，已存在同路径且开启的接口"
}

SUITE_ADD_SUCCESS = {
    'code': '0001',
    'success': True,
    'msg': 'Suite添加成功'
}

SUITE_DEL_SUCCESS = {
    'code': '0003',
    'success': True,
    'msg': 'Suite删除成功'
}

CASE_ADD_SUCCESS = {
    'code': '0001',
    'success': True,
    'msg': '用例添加成功'
}

CASE_EXISTS = {
    'code': '0101',
    'success': False,
    'msg': '此节点下已存在该用例集,请重新命名'
}

CASE_NOT_EXISTS = {
    'code': '0102',
    'success': False,
    'msg': '此用例集不存在'
}

CASE_DELETE_SUCCESS = {
    'code': '0003',
    'success': True,
    'msg': '用例集删除成功'
}

CASE_UPDATE_SUCCESS = {
    'code': '0002',
    'success': True,
    'msg': '用例集更新成功'
}

CONFIG_EXISTS = {
    'code': '0101',
    'success': False,
    'msg': '此配置已存在，请重新命名'
}

VARIABLES_EXISTS = {
    'code': '0101',
    'success': False,
    'msg': '此变量已存在，请重新命名'
}

CONFIG_ADD_SUCCESS = {
    'code': '0001',
    'success': True,
    'msg': '环境添加成功'
}

VARIABLES_ADD_SUCCESS = {
    'code': '0001',
    'success': True,
    'msg': '变量添加成功'
}

CONFIG_NOT_EXISTS = {
    'code': '0102',
    'success': False,
    'msg': '指定的环境不存在'
}

REPORT_NOT_EXISTS = {
    'code': '0102',
    'success': False,
    'msg': '指定的报告不存在'
}

VARIABLES_NOT_EXISTS = {
    'code': '0102',
    'success': False,
    'msg': '指定的全局变量不存在'
}

CONFIG_UPDATE_SUCCESS = {
    'code': '0002',
    'success': True,
    'msg': '环境更新成功'
}

VARIABLES_UPDATE_SUCCESS = {
    'code': '0002',
    'success': True,
    'msg': '全局变量更新成功'
}

TASK_ADD_SUCCESS = {
    'code': '0001',
    'success': True,
    'msg': '定时任务新增成功'
}

TASK_UPDATE_SUCCESS = {
    "code": "0002",
    "success": True,
    "msg": "定时任务更新成功"
}

TASK_UPDATE_EXISTS = {
    "code": "0002",
    "success": False,
    "msg": "定时任务更新失败"
}

TASK_TIME_ILLEGAL = {
    'code': '0101',
    'success': False,
    'msg': '时间表达式非法'
}

TASK_HAS_EXISTS = {
    'code': '0102',
    'success': False,
    'msg': '定时任务已存在'
}

TASK_EMAIL_ILLEGAL = {
    'code': '0102',
    'success': False,
    'msg': '请指定邮件接收人列表'
}

TASK_DEL_SUCCESS = {
    'code': '0003',
    'success': True,
    'msg': '任务删除成功'
}

PLAN_DEL_SUCCESS = {
    'code': '0003',
    'success': True,
    'msg': '集成计划删除成功'
}

PLAN_ADD_SUCCESS = {
    'code': '0001',
    'success': True,
    'msg': '计划添加成功'
}

PLAN_KEY_EXIST = {
    'code': '0101',
    'success': False,
    'msg': '该KEY值已存在，请修改KEY值'
}

PLAN_ILLEGAL = {
    'code': '0101',
    'success': False,
    'msg': '提取字段格式错误，请检查'
}

PLAN_UPDATE_SUCCESS = {
    'code': '0002',
    'success': True,
    'msg': '计划更新成功'
}

HOSTIP_EXISTS = {
    'code': '0101',
    'success': False,
    'msg': '此域名已存在，请重新命名'
}

HOSTIP_ADD_SUCCESS = {
    'code': '0001',
    'success': True,
    'msg': '域名添加成功'
}

HOSTIP_NOT_EXISTS = {
    'code': '0102',
    'success': False,
    'msg': '指定的域名不存在'
}

HOSTIP_UPDATE_SUCCESS = {
    'code': '0002',
    'success': True,
    'msg': '域名更新成功'
}
HOST_DEL_SUCCESS = {
    'code': '0003',
    'success': True,
    'msg': '域名删除成功'
}
TASK_RUN_SUCCESS = {
    'code': '0001',
    'success': True,
    'msg': '手动触发成功，请稍后查看报告'
}
API_SYNC_SUCCESS = {
    'code': '0002',
    'success': True,
    'msg': '用例步骤同步成功'
}

API_SYNC_EXISTS = {
    'code': '0102',
    'success': False,
    'msg': '该用例未在任何用例节点下存在'
}

CASE_STEP_SYNC_SUCCESS = {
    'code': '0002',
    'success': True,
    'msg': 'API同步至用例同步成功'
}

MOCK_VISIT_EXISTS = {
    'code': '0101',
    'success': False,
    'msg': '该接口未配置 OR 状态关闭 OR method错误，请检查!'
}

MOCK_HEADER_EXISTS = {
    'code': '0101',
    'success': False,
    'msg': 'Header错误，请检查!'
}

MOCK_BODY_EXISTS = {
    'code': '0101',
    'success': False,
    'msg': '请求体数据错误!'
}

MOCK_PARAMS_EXISTS = {
    'code': '0101',
    'success': False,
    'msg': 'Params错误!'
}





