# Generated by Django 5.0.4 on 2024-04-08 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='products/')),
                ('category', models.CharField(max_length=50)),
                ('rating', models.FloatField()),
                ('stock', models.IntegerField()),
                ('available', models.BooleanField(default=True)),
                ('production_date', models.DateField(blank=True, null=True)),
                ('country_of_origin', models.CharField(blank=True, max_length=50)),
                ('manufacturer', models.CharField(max_length=100)),
                ('seller', models.CharField(max_length=100)),
                ('anti_counterfeit_code', models.CharField(blank=True, max_length=100)),
                ('serial_number', models.CharField(max_length=50, unique=True)),
            ],
        ),
    ]
