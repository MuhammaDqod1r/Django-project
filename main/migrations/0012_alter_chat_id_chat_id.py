# Generated by Django 3.2.9 on 2021-12-06 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20211206_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat_id',
            name='chat_id',
            field=models.PositiveIntegerField(max_length=50),
        ),
    ]