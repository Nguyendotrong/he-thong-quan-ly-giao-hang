# Generated by Django 3.2.6 on 2021-08-15 08:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('abaShip', '0010_alter_auction_cost'),
    ]

    operations = [
        migrations.RenameField(
            model_name='auction',
            old_name='Active',
            new_name='active',
        ),
    ]
