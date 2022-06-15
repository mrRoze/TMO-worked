from django.db import models

# Create your models here.

from django.db import models


# Create your models here.
class Game(models.Model):
    game_type = models.CharField('Жанр игры', max_length=50)
    game_name = models.CharField('Наименование игры', max_length=50)
    game_photo = models.URLField('Постер игры', max_length=200)

    def __str__(self):
        return f'Жанр: {self.game_type}; Название: {self.game_name}; URL фото: {self.game_photo}'

    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игра'
