# Generated by Django 3.2.4 on 2021-11-19 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poetry_blog', '0002_blog_post_blog_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_post',
            name='blog_images',
            field=models.ImageField(blank=True, upload_to='media'),
        ),
    ]
