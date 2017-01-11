# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('reply_time', models.DateTimeField(default=datetime.datetime.now, null=True, verbose_name=b'reply_time', blank=True)),
                ('reply_content', models.CharField(max_length=300, verbose_name=b'reply_content')),
            ],
            options={
                'db_table': 'bbs_reply',
            },
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=30, verbose_name=b'theme_title')),
                ('theme_content', models.CharField(max_length=300, verbose_name=b'theme_content')),
                ('post_time', models.DateTimeField(default=datetime.datetime.now, null=True, verbose_name=b'post_time', blank=True)),
                ('relay_times', models.IntegerField(default=0, null=True, verbose_name=b'relay_times', blank=True)),
                ('is_set_top', models.IntegerField(default=0, null=True, verbose_name=b'is_set_top', blank=True)),
                ('block', models.BooleanField(default=True, choices=[(1, b'Python'), (0, b'C\xe8\xaf\xad\xe8\xa8\x80'), (3, b'PHP'), (2, b'Java')])),
                ('last_reply_id', models.ForeignKey(blank=True, editable=False, to='apps.Reply', null=True, verbose_name=b'last_reply_id')),
            ],
            options={
                'db_table': 'bbs_theme',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=10, verbose_name=b'name')),
                ('password', models.CharField(max_length=30, verbose_name=b'password')),
            ],
            options={
                'db_table': 'bbs_user',
            },
        ),
        migrations.AddField(
            model_name='theme',
            name='uid',
            field=models.ForeignKey(editable=False, to='apps.User', verbose_name=b'uid'),
        ),
        migrations.AddField(
            model_name='reply',
            name='tid',
            field=models.ForeignKey(editable=False, to='apps.Theme', verbose_name=b'tid'),
        ),
        migrations.AddField(
            model_name='reply',
            name='uid',
            field=models.ForeignKey(editable=False, to='apps.User', verbose_name=b'uid'),
        ),
    ]
