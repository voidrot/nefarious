# Generated by Django 2.1.5 on 2019-05-27 20:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nefarious', '0026_auto_20190527_2029'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='watchmovie',
            name='allow_hardcoded_subs_custom',
        ),
        migrations.RemoveField(
            model_name='watchtvepisode',
            name='allow_hardcoded_subs_custom',
        ),
        migrations.RemoveField(
            model_name='watchtvseason',
            name='allow_hardcoded_subs_custom',
        ),
    ]