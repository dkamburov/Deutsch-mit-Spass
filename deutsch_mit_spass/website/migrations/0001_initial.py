# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TranslationExercise',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('author', models.CharField(max_length=50, default='')),
                ('example', models.CharField(max_length=300)),
                ('translated_example', models.CharField(max_length=300)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('difficulty', models.CharField(choices=[('0', 'low'), ('1', 'easy'), ('2', 'medium'), ('3', 'hard')], max_length=1, default='0')),
                ('content', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ReadingExercise',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('author', models.CharField(max_length=50, default='')),
                ('text', models.TextField()),
                ('question', models.CharField(max_length=300)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CorrectingExercise',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('author', models.CharField(max_length=50, default='')),
                ('correct_sentence', models.CharField(max_length=300)),
                ('wrong_sentence', models.CharField(max_length=300)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('text', models.CharField(max_length=50)),
                ('excercise', models.ForeignKey(to_field='id', to='website.ReadingExercise')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
