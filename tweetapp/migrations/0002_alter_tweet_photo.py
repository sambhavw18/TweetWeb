# Generated by Django 5.0.6 on 2024-07-20 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweetapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='photo',
            field=models.ImageField(null=True, upload_to='photos/'),
        ),
    ]
