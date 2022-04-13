# Generated by Django 3.2.5 on 2022-04-10 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='reviewed',
            field=models.BooleanField(default=False, verbose_name='리뷰작성여부'),
        ),
        migrations.AlterField(
            model_name='order',
            name='delivery_req',
            field=models.CharField(max_length=100, null=True, verbose_name='배송요청사항'),
        ),
        migrations.AlterField(
            model_name='order',
            name='r_pw',
            field=models.CharField(max_length=80, null=True, verbose_name='공동현관비밀번호'),
        ),
    ]
