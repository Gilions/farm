from django.db import models
import uuid


class Product(models.Model):
    guid = models.UUIDField(
        default=uuid.uuid4,
        primary_key=True,
        editable=False
    )
    name = models.CharField(
        verbose_name='Название',
        help_text='Максимальная длина - 255 символов.',
        max_length=255,
        db_index=True
    )
    description = models.TextField(
        verbose_name='Описание',
        help_text='Описание товара.',
        blank=True,
        null=True
    )
    price = models.DecimalField(
        verbose_name='Стоимость',
        max_digits=12,
        decimal_places=2
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name='Активный',
        help_text='Видимость товара'
    )
    image = models.ImageField(
        upload_to='products/',
        verbose_name='Фотография'
    )
    created_at = models.DateTimeField(
        verbose_name='Дата создания.',
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name='Дата последнего обновления.',
        auto_now=True
    )

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['-created_at']

    def __str__(self):
        return self.name
