# Generated by Django 2.1.3 on 2021-01-23 22:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testing_runner', '0002_casestep_source_api_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('creator', models.CharField(max_length=20, null=True, verbose_name='创建人')),
                ('updater', models.CharField(max_length=20, null=True, verbose_name='更新人')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='接口名称')),
                ('request_body', models.TextField(verbose_name='主体信息')),
                ('response_body', models.TextField(verbose_name='主体信息')),
                ('url', models.CharField(max_length=1024, verbose_name='请求地址')),
                ('method', models.CharField(max_length=10, verbose_name='请求方式')),
                ('relation', models.IntegerField(db_index=True, verbose_name='节点id')),
                ('description', models.CharField(max_length=1024, null=True, verbose_name='Mock接口描述')),
                ('status', models.BooleanField(default=False, verbose_name='状态')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testing_runner.Project')),
            ],
            options={
                'verbose_name': 'Mock接口信息',
                'db_table': 'mock',
            },
        ),
    ]
