# Generated by Django 4.0.3 on 2022-03-27 23:41

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0006_rename_author_comment_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.IntegerField(default=1, verbose_name=django.contrib.auth.models.User),
            preserve_default=False,
        ),
    ]
