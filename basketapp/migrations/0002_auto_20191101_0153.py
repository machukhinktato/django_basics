# Generated by Django 2.2.5 on 2019-10-31 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basketapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='add_datetime',
            field=models.DateTimeField(auto_now_add=True, verbose_name='время добавления'),
        ),
    ]
