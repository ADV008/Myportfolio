# Generated by Django 3.0.5 on 2020-04-19 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blog_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='body',
            field=models.TextField(null='True'),
            preserve_default='True',
        ),
    ]
