# Generated by Django 4.1.3 on 2022-11-29 09:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_rename_birhtdate_person_birthdate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='aurthor',
            new_name='author',
        ),
    ]