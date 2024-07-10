# Generated by Django 5.0.6 on 2024-07-02 06:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nagoyameshi', '0007_alter_favorite_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='phone_number',
            field=models.CharField(max_length=11, validators=[django.core.validators.RegexValidator(regex='^[0-9]{10,11}$')], verbose_name='電話番号'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='postal_code',
            field=models.CharField(max_length=8, validators=[django.core.validators.RegexValidator(regex='^[0-9]{3}-[0-9]{4}$')], verbose_name='郵便番号'),
        ),
    ]