# Generated by Django 4.2.3 on 2023-10-15 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OtelApp', '0011_alter_oteloda_roombadcount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oteloda',
            name='roomisempty',
            field=models.BooleanField(default=False, verbose_name='Oda Dolu Mu?'),
        ),
    ]