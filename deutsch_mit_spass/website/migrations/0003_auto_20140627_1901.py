# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_userprofile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='excercise',
            new_name='exercise',
        ),
    ]
