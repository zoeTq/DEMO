# Generated by Django 3.1.5 on 2021-01-16 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testing_runner', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='casestep',
            name='source_api_id',
            field=models.IntegerField(default='1', verbose_name='api来源'),
            preserve_default=False,
        ),
    ]