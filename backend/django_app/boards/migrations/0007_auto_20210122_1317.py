# Generated by Django 3.1.4 on 2021-01-22 11:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0006_post_board'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='board',
        ),
        migrations.AlterField(
            model_name='post',
            name='thread',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='boards.thread', verbose_name='Parent Thread'),
        ),
        migrations.AlterField(
            model_name='thread',
            name='board',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='threads', to='boards.board', verbose_name='Parent Board'),
        ),
    ]
