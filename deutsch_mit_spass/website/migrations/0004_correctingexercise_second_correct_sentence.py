# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20140601_1836'),
    ]

    operations = [
        migrations.AddField(
            model_name='correctingexercise',
            name='second_correct_sentence',
            field=models.CharField(default='', max_length=300),
            preserve_default=True,
        ),
    ]
