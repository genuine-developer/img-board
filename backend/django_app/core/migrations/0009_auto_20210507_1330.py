# Generated by Django 3.1.7 on 2021-05-07 10:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20210507_1327'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='board',
            name='maxThreads',
        ),
        migrations.RemoveField(
            model_name='thread',
            name='maxPosts',
        ),
    ]
