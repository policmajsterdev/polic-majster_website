# Generated by Django 3.2.9 on 2021-11-28 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('konta', '0012_auto_20211128_1316'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profice_pic',
            field=models.ImageField(blank=True, null=True, upload_to='images/profile/'),
        ),
        migrations.AddField(
            model_name='profile',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
