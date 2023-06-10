# Generated by Django 4.2.2 on 2023-06-10 08:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rentacar', '0003_car_availability'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='reservation',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='rentacar.reservation'),
        ),
    ]
