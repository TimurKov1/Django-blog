# Generated by Django 3.2.4 on 2021-07-04 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20210704_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='photo',
            field=models.ImageField(default='photo.png', upload_to='avatars/', verbose_name='Аватар'),
        ),
    ]
