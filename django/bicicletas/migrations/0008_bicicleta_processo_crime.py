# Generated by Django 4.0.4 on 2022-05-04 18:18

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bicicletas', '0007_remove_bicicleta_processo_crime_alter_bicicleta_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='bicicleta',
            name='processo_crime',
            field=models.FileField(default='', storage=django.core.files.storage.FileSystemStorage(location='/media/fotos'), upload_to=''),
            preserve_default=False,
        ),
    ]
