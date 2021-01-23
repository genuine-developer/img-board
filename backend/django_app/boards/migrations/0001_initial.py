# Generated by Django 3.1.4 on 2021-01-22 16:41

import boards.models
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='Unique ID')),
                ('creator', models.CharField(blank=True, default='Anonymous', max_length=255, null=True, verbose_name='Creator')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Update date')),
                ('fileName', models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='File name')),
                ('thumbnail', models.ImageField(blank=True, default=None, null=True, upload_to=boards.models.get_image_upload_to, verbose_name='Thumbnail')),
                ('image', models.ImageField(blank=True, default=None, null=True, upload_to=boards.models.get_image_upload_to, verbose_name='Image')),
                ('isPrivate', models.BooleanField(default=False, verbose_name='Is Private')),
                ('tag', models.CharField(default=None, max_length=10, unique=True, verbose_name='Tag')),
                ('title', models.CharField(default=None, max_length=100, verbose_name='Title')),
                ('description', models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='Description')),
                ('maxThreads', models.IntegerField(default=200, verbose_name='Maximum number of Threads')),
                ('link', models.URLField(blank=True, default=None, null=True, verbose_name='Board link')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='Unique ID')),
                ('creator', models.CharField(blank=True, default='Anonymous', max_length=255, null=True, verbose_name='Creator')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Update date')),
                ('fileName', models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='File name')),
                ('thumbnail', models.ImageField(blank=True, default=None, null=True, upload_to=boards.models.get_image_upload_to, verbose_name='Thumbnail')),
                ('image', models.ImageField(blank=True, default=None, null=True, upload_to=boards.models.get_image_upload_to, verbose_name='Image')),
                ('text', models.TextField(blank=True, default=None, max_length=20000, null=True, verbose_name='Text')),
                ('subject', models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='Subject')),
                ('isPinned', models.BooleanField(default=False, verbose_name='Is Pinned')),
                ('isPruned', models.BooleanField(default=False, verbose_name='Is Pruned')),
                ('maxPosts', models.IntegerField(default=500, verbose_name='Maximum number of Posts')),
                ('board', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='threads', to='boards.board', verbose_name='Parent Board')),
                ('replies', models.ManyToManyField(blank=True, related_name='_thread_replies_+', to='boards.Thread', verbose_name='Replies')),
                ('replies_to', models.ManyToManyField(blank=True, related_name='_thread_replies_to_+', to='boards.Thread', verbose_name='Replies To')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='Unique ID')),
                ('creator', models.CharField(blank=True, default='Anonymous', max_length=255, null=True, verbose_name='Creator')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Update date')),
                ('fileName', models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='File name')),
                ('thumbnail', models.ImageField(blank=True, default=None, null=True, upload_to=boards.models.get_image_upload_to, verbose_name='Thumbnail')),
                ('image', models.ImageField(blank=True, default=None, null=True, upload_to=boards.models.get_image_upload_to, verbose_name='Image')),
                ('text', models.TextField(blank=True, default=None, max_length=20000, null=True, verbose_name='Text')),
                ('board', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='boards.board', verbose_name='Parent Board')),
                ('replies', models.ManyToManyField(blank=True, related_name='_post_replies_+', to='boards.Post', verbose_name='Replies')),
                ('replies_to', models.ManyToManyField(blank=True, related_name='_post_replies_to_+', to='boards.Post', verbose_name='Replies To')),
                ('thread', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='boards.thread', verbose_name='Parent Thread')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
