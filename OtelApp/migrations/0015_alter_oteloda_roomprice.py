# Generated by Django 4.2.6 on 2023-10-18 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OtelApp', '0014_alter_konukbilgileri_guest_tc_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oteloda',
            name='roomprice',
            field=models.IntegerField(blank=True, default=0, verbose_name='Odanın Fiyatı'),
        ),
    ]
