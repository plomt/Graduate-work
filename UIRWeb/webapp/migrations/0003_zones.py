# Generated by Django 3.2.9 on 2021-12-19 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_pins'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zone1_x', models.FloatField()),
                ('zone1_y', models.FloatField()),
                ('zone1_d', models.FloatField()),
                ('zone2_x', models.FloatField()),
                ('zone2_y', models.FloatField()),
                ('zone2_d', models.FloatField()),
                ('zone3_x', models.FloatField()),
                ('zone3_y', models.FloatField()),
                ('zone3_d', models.FloatField()),
                ('zone4_x', models.FloatField()),
                ('zone4_y', models.FloatField()),
                ('zone4_d', models.FloatField()),
            ],
        ),
    ]
