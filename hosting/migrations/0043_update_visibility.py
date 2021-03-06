# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-17 10:47
from __future__ import unicode_literals

from django.db import migrations


def create_visibility_settings(app_registry, schema_editor):
    PubModel = app_registry.get_model('hosting', 'VisibilitySettings')
    ContentType = app_registry.get_model('contenttypes', 'ContentType')

    Profile = app_registry.get_model('hosting', 'Profile')
    Profile_CT = ContentType.objects.get_for_model(Profile)
    for profile in Profile.all_objects.only('pk').all():
        pub = PubModel(
            model_type='PublicEmail', model_id=profile.pk, content_type=Profile_CT,
            visible_online_public=False, visible_online_authed=False, visible_in_book=True)
        pub.save()
        profile.email_visibility_id = pub.pk
        profile.save(update_fields=['email_visibility'])

    Place = app_registry.get_model('hosting', 'Place')
    Place_CT = ContentType.objects.get_for_model(Place)
    for place in Place.all_objects.only('pk').all():
        pub = PubModel(
            model_type='Place', model_id=place.pk, content_type=Place_CT,
            visible_online_public=True, visible_online_authed=True, visible_in_book=True)
        pub.save()
        place.visibility_id = pub.pk
        fmpub = PubModel(
            model_type='FamilyMembers', model_id=place.pk, content_type=Place_CT,
            visible_online_public=False, visible_online_authed=True, visible_in_book=True)
        fmpub.save()
        place.family_members_visibility_id = fmpub.pk
        place.save(update_fields=['visibility', 'family_members_visibility'])

    Phone = app_registry.get_model('hosting', 'Phone')
    Phone_CT = ContentType.objects.get_for_model(Phone)
    for phone in Phone.all_objects.only('pk').all():
        pub = PubModel(
            model_type='Phone', model_id=phone.pk, content_type=Phone_CT,
            visible_online_public=False, visible_online_authed=True, visible_in_book=True)
        pub.save()
        phone.visibility_id = pub.pk
        phone.save(update_fields=['visibility'])


class Migration(migrations.Migration):

    dependencies = [
        ('hosting', '0042_create_visibility'),
    ]

    operations = [
        migrations.RunPython(create_visibility_settings, reverse_code=migrations.RunPython.noop),
    ]
