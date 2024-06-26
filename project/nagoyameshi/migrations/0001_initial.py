# Generated by Django 5.0.6 on 2024-06-24 07:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExtendedModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_at', models.DateTimeField(auto_now=True, null=True, verbose_name='論理削除日')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='更新日')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日')),
            ],
        ),
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='曜日')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('extendedmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='nagoyameshi.extendedmodel')),
                ('name', models.CharField(max_length=15, verbose_name='カテゴリ名')),
            ],
            bases=('nagoyameshi.extendedmodel',),
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('extendedmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='nagoyameshi.extendedmodel')),
                ('name', models.CharField(max_length=30, verbose_name='店舗名')),
                ('description', models.CharField(max_length=500, verbose_name='店舗説明')),
                ('floor_price', models.PositiveIntegerField(verbose_name='下限価格')),
                ('maximum_price', models.PositiveIntegerField(verbose_name='上限価格')),
                ('opening_time', models.DateTimeField(verbose_name='開店時刻')),
                ('closing_time', models.DateTimeField(verbose_name='閉店時刻')),
                ('postal_code', models.CharField(max_length=8, verbose_name='郵便番号')),
                ('city', models.CharField(max_length=50, verbose_name='市区町村')),
                ('street_address', models.CharField(max_length=50, verbose_name='番地以降住所')),
                ('phone_number', models.CharField(max_length=11, verbose_name='電話番号')),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='nagoyameshi.category', verbose_name='カテゴリー')),
                ('regular_closing_day', models.ManyToManyField(to='nagoyameshi.day', verbose_name='定休日')),
            ],
            bases=('nagoyameshi.extendedmodel',),
        ),
    ]
