# Generated by Django 5.0.6 on 2024-06-29 02:16

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nagoyameshi', '0002_alter_restaurant_closing_time_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('extendedmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='nagoyameshi.extendedmodel')),
                ('comment', models.CharField(max_length=800, verbose_name='コメント')),
                ('visited_date', models.DateField(verbose_name='利用日')),
                ('restaurant_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nagoyameshi.restaurant', verbose_name='店舗')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='投稿者')),
            ],
            bases=('nagoyameshi.extendedmodel',),
        ),
    ]
