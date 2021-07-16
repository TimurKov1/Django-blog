# Generated by Django 3.2.4 on 2021-07-05 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_userprofile_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='username',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='photo',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(default='avatar.jpg', upload_to='avatars/', verbose_name='Аватар'),
        ),
    ]
