# Generated by Django 2.0.5 on 2018-05-11 14:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, default='no-slug', max_length=160)),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('last_mod_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='修改时间')),
                ('title', models.CharField(max_length=200, unique=True, verbose_name='标题')),
                ('body', models.TextField(verbose_name='正文')),
                ('pub_time', models.DateTimeField(blank=True, null=True, verbose_name='发布时间')),
                ('status', models.CharField(choices=[('d', '草稿'), ('p', '发表')], default='p', max_length=1, verbose_name='文章状态')),
                ('comment_status', models.CharField(choices=[('o', '打开'), ('c', '关闭')], default='o', max_length=1, verbose_name='评论状态')),
                ('type', models.CharField(choices=[('a', '文章'), ('p', '页面')], default='a', max_length=1, verbose_name='类型')),
                ('views', models.PositiveIntegerField(default=0, verbose_name='浏览量')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='作者')),
            ],
            options={
                'ordering': ['-pub_time'],
                'verbose_name_plural': '文章',
                'verbose_name': '文章',
                'get_latest_by': 'created_time',
            },
        ),
        migrations.CreateModel(
            name='BlogSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sitename', models.CharField(default='', max_length=200, verbose_name='网站名称')),
                ('site_description', models.TextField(default='', max_length=1000, verbose_name='网站描述')),
                ('site_seo_description', models.TextField(default='', max_length=1000, verbose_name='网站SEO描述')),
                ('site_keywords', models.TextField(default='', max_length=1000, verbose_name='网站关键字')),
                ('article_sub_length', models.IntegerField(default=300, verbose_name='文章摘要长度')),
                ('sidebar_article_count', models.IntegerField(default=10, verbose_name='侧边栏文章数目')),
                ('sidebar_comment_count', models.IntegerField(default=5, verbose_name='侧边栏评论数目')),
                ('show_google_adsense', models.BooleanField(default=False, verbose_name='是否显示谷歌广告')),
                ('google_adsense_codes', models.TextField(blank=True, default='', max_length=2000, null=True, verbose_name='广告内容')),
                ('open_site_comment', models.BooleanField(default=True, verbose_name='是否打开网站评论功能')),
                ('beiancode', models.CharField(blank=True, default='', max_length=2000, null=True, verbose_name='备案号')),
                ('analyticscode', models.TextField(default='', max_length=1000, verbose_name='网站统计代码')),
                ('gongan_beiancode', models.TextField(blank=True, default='', max_length=2000, null=True, verbose_name='公安备案号')),
            ],
            options={
                'verbose_name_plural': '网站配置',
                'verbose_name': '网站配置',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, default='no-slug', max_length=160)),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('last_mod_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='修改时间')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='分类名')),
                ('parent_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Category', verbose_name='父级分类')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name_plural': '分类',
                'verbose_name': '分类',
            },
        ),
        migrations.CreateModel(
            name='Links',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='链接名称')),
                ('link', models.URLField(verbose_name='链接地址')),
                ('sequence', models.IntegerField(unique=True, verbose_name='排序')),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('last_mod_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='修改时间')),
            ],
            options={
                'ordering': ['sequence'],
                'verbose_name_plural': '友情链接',
                'verbose_name': '友情链接',
            },
        ),
        migrations.CreateModel(
            name='SideBar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='标题')),
                ('content', models.TextField(verbose_name='内容')),
                ('sequence', models.IntegerField(unique=True, verbose_name='排序')),
                ('is_enable', models.BooleanField(default=True, verbose_name='是否启用')),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('last_mod_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='修改时间')),
            ],
            options={
                'ordering': ['sequence'],
                'verbose_name_plural': '侧边栏',
                'verbose_name': '侧边栏',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, default='no-slug', max_length=160)),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('last_mod_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='修改时间')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='标签名')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name_plural': '标签',
                'verbose_name': '标签',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Category', verbose_name='分类'),
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(blank=True, to='blog.Tag', verbose_name='标签集合'),
        ),
    ]
