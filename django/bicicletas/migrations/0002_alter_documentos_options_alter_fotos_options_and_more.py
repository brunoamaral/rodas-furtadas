# Generated by Django 4.0.4 on 2022-05-02 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bicicletas', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='documentos',
            options={'managed': True, 'verbose_name_plural': 'Documentos'},
        ),
        migrations.AlterModelOptions(
            name='fotos',
            options={'managed': True, 'verbose_name_plural': 'Fotos'},
        ),
        migrations.AddField(
            model_name='bicicleta',
            name='email',
            field=models.EmailField(default='', max_length=280),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bicicleta',
            name='nro_serie',
            field=models.CharField(blank=True, max_length=280, null=True, unique=True),
        ),
    ]
