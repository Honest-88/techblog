# Generated by Django 3.0.6 on 2020-05-20 23:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_post_slider_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='slider_post',
        ),
    ]
