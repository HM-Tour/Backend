# Generated by Django 4.1.4 on 2023-01-20 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='owner',
            field=models.TextField(),
        ),
    ]
