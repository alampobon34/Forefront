# Generated by Django 4.0 on 2022-01-05 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foreFrontApp', '0004_news'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='description',
            field=models.TextField(max_length=1000),
        ),
    ]
