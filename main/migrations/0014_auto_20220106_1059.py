# Generated by Django 3.2.9 on 2022-01-06 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_alter_chat_id_chat_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='background_image',
            field=models.ImageField(upload_to='banner_images/'),
        ),
        migrations.AlterField(
            model_name='brand',
            name='image',
            field=models.ImageField(upload_to='brands/'),
        ),
        migrations.AlterField(
            model_name='call06',
            name='background_image',
            field=models.ImageField(upload_to='call06/'),
        ),
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=models.ImageField(upload_to='site_logos/'),
        ),
        migrations.AlterField(
            model_name='content21_obj',
            name='image',
            field=models.ImageField(upload_to='content_21_obj/'),
        ),
        migrations.AlterField(
            model_name='content21_obj2',
            name='image',
            field=models.ImageField(upload_to='content_21_obj2/'),
        ),
        migrations.AlterField(
            model_name='content21_text',
            name='image',
            field=models.ImageField(upload_to='content_21_text/'),
        ),
        migrations.AlterField(
            model_name='content22_section1',
            name='image',
            field=models.ImageField(upload_to='content22_section1/'),
        ),
        migrations.AlterField(
            model_name='content22_section1_obj',
            name='image',
            field=models.ImageField(upload_to='content22_section1_obj/'),
        ),
        migrations.AlterField(
            model_name='content22_section2',
            name='image',
            field=models.ImageField(upload_to='content22_section2/'),
        ),
        migrations.AlterField(
            model_name='content22_section2_obj',
            name='image',
            field=models.ImageField(upload_to='content22_section2_obj/'),
        ),
        migrations.AlterField(
            model_name='content22_section3',
            name='image',
            field=models.ImageField(upload_to='content22_section3/'),
        ),
        migrations.AlterField(
            model_name='content22_section3_obj',
            name='image',
            field=models.ImageField(upload_to='content22_section3_obj/'),
        ),
        migrations.AlterField(
            model_name='content23',
            name='background_image',
            field=models.ImageField(upload_to='content23/'),
        ),
        migrations.AlterField(
            model_name='download01_form_text',
            name='image',
            field=models.ImageField(upload_to='download_form_text/'),
        ),
        migrations.AlterField(
            model_name='features06_obj',
            name='image',
            field=models.ImageField(upload_to='feauters_obj/'),
        ),
        migrations.AlterField(
            model_name='features06_text',
            name='image',
            field=models.ImageField(upload_to='feauters_text/'),
        ),
        migrations.AlterField(
            model_name='introduction_video',
            name='video',
            field=models.FileField(upload_to='videos/'),
        ),
        migrations.AlterField(
            model_name='portfolio07_image',
            name='image',
            field=models.ImageField(upload_to='portfolio007_image/'),
        ),
        migrations.AlterField(
            model_name='portfolio07_obj',
            name='image',
            field=models.ImageField(upload_to='portfolio007obj/'),
        ),
        migrations.AlterField(
            model_name='testimonals_text',
            name='image',
            field=models.ImageField(upload_to='testimonals_text/'),
        ),
    ]
