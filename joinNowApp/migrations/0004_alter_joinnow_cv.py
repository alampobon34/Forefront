# Generated by Django 4.0 on 2022-01-01 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joinNowApp', '0003_alter_joinnow_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joinnow',
            name='CV',
            field=models.FileField(blank=True, upload_to='CV_Files'),
        ),
    ]
