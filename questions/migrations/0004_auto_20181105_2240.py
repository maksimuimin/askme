# Generated by Django 2.1.2 on 2018-11-05 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0003_auto_20181105_0029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='media/default_user_avatar.png', upload_to='media/user_avatars'),
        ),
    ]
