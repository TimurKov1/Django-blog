from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class UserProfile(models.Model):
    user = models.OneToOneField(User, verbose_name='Имя', on_delete=models.CASCADE, default='name')
    avatar = models.ImageField('Аватар', default='avatar.png', upload_to='avatars/')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        photo = Image.open(self.avatar.path)

        if photo.width > 150 and photo.height > 150:
            resize = (200, 200)
            photo.thumbnail(resize) 
            photo.save(self.avatar.path)
    
    def __str__(self):
        return f'{self.user.username}'

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'