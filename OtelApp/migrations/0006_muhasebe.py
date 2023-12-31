# Generated by Django 4.2.3 on 2023-10-12 02:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('OtelApp', '0005_oteloda_roomisempty'),
    ]

    operations = [
        migrations.CreateModel(
            name='Muhasebe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Tarih')),
                ('calculate', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Fatura Tutarı')),
                ('guest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OtelApp.konukbilgileri', verbose_name='Müşteri')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OtelApp.oteloda', verbose_name='Oda')),
            ],
        ),
    ]
