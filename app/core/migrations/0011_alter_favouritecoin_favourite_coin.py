# Generated by Django 4.0.1 on 2022-03-13 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_rename_favourite_favouritecoin_favourite_coin_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favouritecoin',
            name='favourite_coin',
            field=models.CharField(max_length=20),
        ),
    ]
