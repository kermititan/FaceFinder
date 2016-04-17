# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-17 21:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import slave.models


class Migration(migrations.Migration):

    dependencies = [
        ('slave', '0004_remove_person_photos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.ImageField(upload_to=slave.models.refpictures_directory_path)),
            ],
        ),
        migrations.RenameField(
            model_name='person',
            old_name='picture',
            new_name='main_picture',
        ),
        migrations.AddField(
            model_name='picture',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='slave.Person'),
        ),
    ]