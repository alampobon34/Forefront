# Generated by Django 4.0 on 2022-01-01 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foreFrontApp', '0002_contactus'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsTeller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]