# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-17 10:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hosting', '0043_update_visibility'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visibilitysettings',
            name='content_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='email_visibility',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='profile', to='hosting.VisibilitySettingsForPublicEmail'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='visibility',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='phone', to='hosting.VisibilitySettingsForPhone'),
        ),
        migrations.AlterField(
            model_name='place',
            name='visibility',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='place', to='hosting.VisibilitySettingsForPlace'),
        ),
        migrations.AlterField(
            model_name='place',
            name='family_members_visibility',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='family_members', to='hosting.VisibilitySettingsForFamilyMembers'),
        ),
    ]
