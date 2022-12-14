# Generated by Django 4.1.3 on 2022-11-26 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('misc', '0002_fix_site_tettings'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesettings',
            name='maps_link',
            field=models.CharField(blank=True, help_text='Ссылку можно получить используя ресурс https://yandex.ru/map-constructor/', max_length=1000, null=True, verbose_name='Ссылка на карту'),
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='city_type',
            field=models.CharField(choices=[('Город', 'Город'), ('Деревня', 'Деревня'), ('Поселок', 'Поселок')], default='Город', help_text='Выбрать из предложенных.', max_length=15, verbose_name='Тип поселения'),
        ),
    ]
