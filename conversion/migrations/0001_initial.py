# Generated by Django 5.0.4 on 2024-04-24 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CURRENCY_RATE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency', models.CharField(max_length=4, unique=True)),
                ('rate', models.FloatField()),
            ],
        ),
    ]