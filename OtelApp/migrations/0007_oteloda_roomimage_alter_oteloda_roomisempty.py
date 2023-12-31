# Generated by Django 4.2.3 on 2023-10-13 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OtelApp', '0006_muhasebe'),
    ]

    operations = [
        migrations.AddField(
            model_name='oteloda',
            name='roomimage',
            field=models.ImageField(default=1, upload_to='rooms', verbose_name='Oda Resmi'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='oteloda',
            name='roomisempty',
            field=models.BooleanField(default=True, verbose_name='Oda Dolu Mu?'),
        ),
    ]
