# Generated by Django 3.0.4 on 2020-03-16 07:22

from django.db import migrations, models
import file_app.validators


class Migration(migrations.Migration):

    dependencies = [
        ('file_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.FileField(upload_to='', validators=[file_app.validators.validate_file_extension]),
        ),
    ]
