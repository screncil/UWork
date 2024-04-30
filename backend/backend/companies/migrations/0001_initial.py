# Generated by Django 5.0.4 on 2024-04-29 16:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cities', '0001_initial'),
        ('countries', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('phone', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cities.cities')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='countries.countries')),
            ],
        ),
    ]
