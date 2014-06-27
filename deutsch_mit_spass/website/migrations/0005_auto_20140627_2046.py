# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_auto_20140627_2046'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='correct',
            new_name='is_correct',
        ),
    ]
