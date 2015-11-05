# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('answer', models.TextField(blank=True, max_length=600, null=True)),
                ('date_answer', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('question', models.TextField(max_length=300)),
                ('date_question', models.DateTimeField(auto_now_add=True)),
                ('user_from', models.ForeignKey(related_name='questions_from', to=settings.AUTH_USER_MODEL)),
                ('user_to', models.ForeignKey(related_name='questions_to', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(related_name='answers', to='answer.Question'),
        ),
    ]
