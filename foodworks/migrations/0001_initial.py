# Generated by Django 3.2.13 on 2022-06-08 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='foodrecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=30)),
                ('item_type', models.CharField(max_length=30)),
                ('item_price', models.CharField(max_length=30)),
                ('stock_available', models.CharField(max_length=30)),
            ],
        ),
    ]
