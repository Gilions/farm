from django.db import models
from solo.models import SingletonModel


class LocalType(models.TextChoices):
    CITY = ('Город', 'Город')
    VILLAGE = ('Деревня', 'Деревня')
    TOWNSHIP = ('Поселок', 'Поселок')


class SiteSettings(SingletonModel):
    company_name = models.CharField(
        verbose_name='Название компании',
        help_text='Максимальная длина названия 60 символов.',
        max_length=60
    )
    phone_number = models.CharField(
        verbose_name='Телефон',
        help_text='Максимальная длина 120 символов.',
        max_length=120
    )
    whatsapp = models.CharField(
        verbose_name='WhatsApp',
        help_text='Максимальная длина 120 символов.',
        max_length=120,
        blank=True,
        null=True
    )
    telegram = models.CharField(
        verbose_name='Telegram',
        help_text='Максимальная длина 120 символов.',
        max_length=120,
        blank=True,
        null=True
    )
    email = models.EmailField(
        verbose_name='e-Mail',
        help_text='Электронная почта компании.'
    )
    region = models.CharField(
        verbose_name='Область',
        help_text='Максимальная длина 120 символов.',
        max_length=120
    )
    city_type = models.CharField(
        verbose_name='Тип поселения',
        help_text='Выбрать из предложенных.',
        max_length=15,
        choices=LocalType.choices,
        default=LocalType.CITY
    )
    city = models.CharField(
        verbose_name='Город',
        help_text='Название города, максимальная длина 120 символов.',
        max_length=120
    )
    street = models.CharField(
        verbose_name='Адрес',
        help_text='Адрес, максимальная длина 500.',
        max_length=500
    )
    index = models.CharField(
        verbose_name='Индекс',
        help_text='Индекс, максимальная длина 10.',
        max_length=10
    )
    maps_link = models.CharField(
        verbose_name='Ссылка на карту',
        help_text='Ссылку можно получить используя ресурс https://yandex.ru/map-constructor/',
        max_length=1000,
        blank=True,
        null=True
    )
    head_title = models.CharField(
        verbose_name='Шапка, заглавие',
        help_text='Заглавие основной страницы, максимальная длина 30 символов.',
        max_length=30
    )
    head_description = models.TextField(
        verbose_name='Шапка, описание',
        help_text='Описание основной страницы, максимальная длина 300 символов.',
        max_length=300
    )

    class Meta:
        verbose_name = 'Настройки сайта'
        verbose_name_plural = 'Настройки сайта'

    def __str__(self):
        return self.company_name
