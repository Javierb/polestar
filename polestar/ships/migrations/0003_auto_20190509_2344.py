# Generated by Django 2.2.1 on 2019-05-09 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ships', '0002_auto_20190509_2139'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='position',
            name='imo_number',
        ),
        migrations.AddField(
            model_name='ship',
            name='positions',
            field=models.ManyToManyField(to='ships.Position'),
        ),
    ]
