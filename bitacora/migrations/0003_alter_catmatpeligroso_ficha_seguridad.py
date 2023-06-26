# Generated by Django 4.0 on 2023-06-25 22:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bitacora', '0002_alter_catmatpeligroso_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catmatpeligroso',
            name='ficha_seguridad',
            field=models.FileField(blank=True, null=True, upload_to='fichas_seguridad/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])]),
        ),
    ]