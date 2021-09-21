# Generated by Django 3.2.6 on 2021-09-21 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abaShip', '0007_alter_ordership_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordershipdetail',
            name='pay_method',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Zalo pay'), (1, 'Momo'), (2, 'Tien Mat')], default=2),
        ),
    ]