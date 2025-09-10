from django.db import models


class Toy(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name='Название')
    description = models.TextField(
        verbose_name='Описание',
    )
    slug = models.SlugField(unique=True)
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Цена',
    )
    is_available = models.BooleanField(
        default=True,
        verbose_name='В наличии',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Игрушка'
        verbose_name_plural = 'Игрушки'

    def __str__(self) -> str:
        return f'Игрушка {self.name}'


class ToyImage(models.Model):
    toy = models.ForeignKey(
        Toy,
        on_delete=models.CASCADE,
        related_name='images',
    )
    image = models.ImageField(
        upload_to='toys/images/%Y/%m/%d/',
        verbose_name='Изображение',
    )
    is_main = models.BooleanField(
        default=False,
        verbose_name='Основное изображение',
    )

    class Meta:
        verbose_name = 'Фото игрушки'
        verbose_name_plural = 'Фото игрушек'

    def __str__(self):
        return f'Фото для {self.toy.name}'
