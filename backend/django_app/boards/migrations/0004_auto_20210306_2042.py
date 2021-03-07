# Generated by Django 3.1.4 on 2021-03-06 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0003_auto_20210126_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='creator',
            field=models.CharField(blank=True, default='Anonymous', max_length=30, null=True, verbose_name='Creator'),
        ),
        migrations.AlterField(
            model_name='post',
            name='creator',
            field=models.CharField(blank=True, default='Anonymous', max_length=30, null=True, verbose_name='Creator'),
        ),
        migrations.AlterField(
            model_name='thread',
            name='creator',
            field=models.CharField(blank=True, default='Anonymous', max_length=30, null=True, verbose_name='Creator'),
        ),
    ]