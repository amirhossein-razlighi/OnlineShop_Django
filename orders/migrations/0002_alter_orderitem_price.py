# Generated by Django 3.2.6 on 2021-08-19 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='price',
            field=models.IntegerField(),
        ),
    ]
