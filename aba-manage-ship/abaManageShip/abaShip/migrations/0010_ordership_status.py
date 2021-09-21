# Generated by Django 3.2.6 on 2021-09-21 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abaShip', '0009_auto_20210922_0026'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordership',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(0, 'not yet shipped'), (1, 'shipping'), (2, 'shipped')], default=0),
        ),
    ]