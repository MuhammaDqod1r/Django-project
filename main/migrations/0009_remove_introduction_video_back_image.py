# Generated by Django 3.2.9 on 2021-12-03 09:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_rename_video_url_introduction_video_video'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='introduction_video',
            name='back_image',
        ),
    ]
