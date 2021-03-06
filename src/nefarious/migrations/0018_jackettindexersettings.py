# Generated by Django 2.1.1 on 2019-01-06 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nefarious', '0017_auto_20181219_2010'),
    ]

    operations = [
        migrations.CreateModel(
            name='JackettIndexerSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('indexer', models.CharField(max_length=200, unique=True)),
                ('ratio_management', models.CharField(choices=[('download & seed', 'download & seed'), ('seed', 'seed')], max_length=100)),
            ],
        ),
    ]
