# Generated by Django 5.0.6 on 2024-07-07 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nagoyameshi', '0009_reservation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='comment',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='コメント'),
        ),
    ]