# Generated by Django 4.1.5 on 2023-01-15 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_alter_post_options_alter_post_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='owner',
        ),
    ]
