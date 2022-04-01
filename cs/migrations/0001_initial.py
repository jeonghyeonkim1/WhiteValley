# Generated by Django 3.2.5 on 2022-04-01 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=30, verbose_name='게시글 종류')),
                ('title', models.CharField(max_length=60, verbose_name='제목')),
                ('content', models.TextField(blank=True, verbose_name='내용')),
                ('reg_date', models.DateTimeField(auto_now_add=True, verbose_name='작성일')),
                ('view_cnt', models.IntegerField(default=0, verbose_name='조회수')),
                ('e_start', models.DateField(null=True, verbose_name='이벤트 시작일')),
                ('e_end', models.DateField(null=True, verbose_name='이벤트 종료일')),
            ],
            options={
                'verbose_name': '게시글',
                'verbose_name_plural': '게시글(들)',
                'db_table': 't_board',
            },
        ),
    ]
