from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Record(models.Model):
    title = models.CharField('Название', max_length=150)
    message = models.TextField('Запись')
    date = models.DateTimeField('Дата', default=timezone.now)
    author = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE)
    photo = models.ImageField('Фото', default='', upload_to='photos/')

    class Meta():
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'