# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, to_field='id', unique=True)),
                ('role', models.SmallIntegerField(choices=[(0, 'Student'), (1, 'Teacher')], default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
