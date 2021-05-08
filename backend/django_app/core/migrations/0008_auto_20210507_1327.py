# Generated by Django 3.1.7 on 2021-05-07 10:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20210507_1312'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='likes',
            new_name='likesCount',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='posts',
            new_name='postsCount',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='shares',
            new_name='sharesCount',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='views',
            new_name='viewsCount',
        ),
        migrations.RenameField(
            model_name='thread',
            old_name='likes',
            new_name='likesCount',
        ),
        migrations.RenameField(
            model_name='thread',
            old_name='posts',
            new_name='postsCount',
        ),
        migrations.RenameField(
            model_name='thread',
            old_name='shares',
            new_name='sharesCount',
        ),
        migrations.RenameField(
            model_name='thread',
            old_name='views',
            new_name='viewsCount',
        ),
        migrations.AlterField(
            model_name='post',
            name='board',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='core.board', verbose_name='Board'),
        ),
        migrations.AlterField(
            model_name='post',
            name='repliesto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='core.post', verbose_name='Replies To'),
        ),
        migrations.AlterField(
            model_name='post',
            name='thread',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='core.thread', verbose_name='Thread'),
        ),
    ]