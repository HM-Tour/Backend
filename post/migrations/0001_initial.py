# Generated by Django 4.1.5 on 2023-01-24 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('rate', models.IntegerField(default=5)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('location', models.TextField()),
                ('price', models.FloatField()),
            ],
            options={
                'ordering': ['-pk'],
            },
        ),
    ]
