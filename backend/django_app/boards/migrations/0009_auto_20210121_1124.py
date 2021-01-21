# Generated by Django 3.1.4 on 2021-01-21 09:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0008_auto_20210120_2027'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='board',
            name='threads',
        ),
        migrations.AddField(
            model_name='board',
            name='threads',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='boards.thread'),
        ),
        migrations.RemoveField(
            model_name='thread',
            name='posts',
        ),
        migrations.AddField(
            model_name='thread',
            name='posts',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='boards.post'),
        ),
    ]