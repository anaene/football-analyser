# Generated by Django 3.0.8 on 2020-07-26 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Confederation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('abbreviation', models.CharField(max_length=12, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('region', models.CharField(max_length=50)),
            ],
        ),
    ]