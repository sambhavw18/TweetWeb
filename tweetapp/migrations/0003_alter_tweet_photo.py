# Generated by Django 5.0.6 on 2024-07-20 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweetapp', '0002_alter_tweet_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='photos/'),
        ),
    ]
