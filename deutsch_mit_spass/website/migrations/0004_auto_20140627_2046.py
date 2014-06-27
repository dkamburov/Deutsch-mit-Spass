# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20140627_1901'),
    ]

    operations = [
        migrations.CreateModel(
            name='FillInExercise',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('example', models.CharField(max_length=300)),
                ('correct_answer', models.CharField(max_length=20)),
                ('wrong_answer', models.CharField(max_length=20)),
                ('second_wrong_answer', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OrderingExercise',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('description', models.CharField(max_length=50)),
                ('first', models.CharField(max_length=20)),
                ('second', models.CharField(max_length=20)),
                ('third', models.CharField(max_length=20)),
                ('fourt', models.CharField(max_length=20)),
                ('first_match', models.CharField(max_length=20)),
                ('second_match', models.CharField(max_length=20)),
                ('third_match', models.CharField(max_length=20)),
                ('fourt_match', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='choice',
            name='correct',
            field=models.SmallIntegerField(choices=[(0, 'False'), (1, 'True')], default=0),
            preserve_default=True,
        ),
    ]
