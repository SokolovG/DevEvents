# Generated by Django 5.1.4 on 2025-01-12 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=25)),
                ('slug', models.SlugField(max_length=25, unique=True)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('text', models.TextField(max_length=25)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=25)),
                ('description', models.TextField(max_length=1000)),
                ('pub_date', models.DateTimeField()),
                ('is_published', models.BooleanField()),
                ('event_start_date', models.DateTimeField()),
                ('event_end_date', models.DateTimeField()),
                ('is_online', models.BooleanField()),
                ('meeting_link', models.URLField()),
                ('is_verify', models.BooleanField()),
                ('max_participants', models.PositiveIntegerField(blank=True)),
                ('registration_deadline', models.DateTimeField(blank=True)),
                ('format', models.CharField(max_length=25)),
                ('members', models.PositiveIntegerField(blank=True)),
                ('photos', models.ImageField(upload_to='')),
                ('you_are_member', models.BooleanField()),
            ],
            options={
                'ordering': ['event_start_date'],
            },
        ),
        migrations.CreateModel(
            name='EventRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=25)),
                ('address', models.CharField(blank=True, max_length=100)),
                ('city', models.CharField(max_length=25)),
                ('country', models.CharField(max_length=25)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
