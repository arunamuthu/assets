# Generated by Django 3.0.4 on 2020-04-06 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('file_app', '0004_auto_20200406_1206'),
    ]

    operations = [
        migrations.RenameField(
            model_name='type',
            old_name='name',
            new_name='type',
        ),
        migrations.RenameField(
            model_name='typearea',
            old_name='name',
            new_name='typearea',
        ),
    ]
