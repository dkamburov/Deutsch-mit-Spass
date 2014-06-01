# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='readingexercise',
            name='author',
        ),
        migrations.RemoveField(
            model_name='translationexercise',
            name='author',
        ),
        migrations.RemoveField(
            model_name='correctingexercise',
            name='author',
        ),
    ]
