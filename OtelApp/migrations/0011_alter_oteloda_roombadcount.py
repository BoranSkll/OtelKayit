# Generated by Django 4.2.3 on 2023-10-15 02:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OtelApp', '0010_alter_oteloda_roombadcount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oteloda',
            name='roombadcount',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1, message='En Az Bir Yatak Olmalıdır!'), django.core.validators.MaxValueValidator(6, message='6 Yataktan Daha Fazla Ekleyemezsin!')], verbose_name='Oda Yatak Sayısı'),
        ),
    ]
