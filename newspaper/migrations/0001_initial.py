# Generated by Django 3.0.4 on 2020-03-20 06:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='news_category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('sorting', models.CharField(max_length=15)),
                ('enabled_category', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '뉴스 카테고리',
            },
        ),
        migrations.CreateModel(
            name='news_comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(verbose_name='댓글')),
                ('comment_nickname', models.CharField(max_length=25)),
                ('comment_password', models.CharField(max_length=8)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '뉴스 댓글',
            },
        ),
        migrations.CreateModel(
            name='news_article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='기사 제목')),
                ('content', models.TextField(verbose_name='기사 내용')),
                ('video_link', models.CharField(max_length=200)),
                ('published_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('public', models.BooleanField(default=True)),
                ('views', models.IntegerField(default=0)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='newspaper.news_category')),
            ],
            options={
                'verbose_name': '뉴스 기사',
                'verbose_name_plural': '뉴스 기사들',
            },
        ),
    ]
