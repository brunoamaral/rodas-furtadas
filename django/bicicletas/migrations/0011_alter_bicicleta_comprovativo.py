# Generated by Django 4.0.4 on 2022-05-12 13:23

import bicicletas.models
import django.core.files.storage
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bicicletas', '0010_bicicleta_razao_registo_alter_bicicleta_comprovativo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bicicleta',
            name='comprovativo',
            field=models.FileField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(location='/media/'), upload_to='', validators=[bicicletas.models.file_size, django.core.validators.FileExtensionValidator(['pdf', 'jpeg', 'jpg'])]),
        ),
    ]
