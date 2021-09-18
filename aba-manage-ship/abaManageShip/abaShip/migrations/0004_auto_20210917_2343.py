# Generated by Django 3.2.6 on 2021-09-17 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abaShip', '0003_auto_20210917_2016'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_finish',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default=0, max_length=10),
        ),
    ]