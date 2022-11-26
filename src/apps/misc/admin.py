from django.contrib import admin
from solo.admin import SingletonModelAdmin

from apps.misc.models import SiteSettings


@admin.register(SiteSettings)
class SiteSettingsAdmin(SingletonModelAdmin):
    fieldsets = (
        ('Индексная страница', {
            'fields': (
                'head_title',
                'head_description'
            ),
        }),
        ('Данные компании', {
            'fields': (
                'company_name',
                'region',
                'city_type',
                'city',
                'street',
                'index',
                'maps_link'
            ),
        }),
        (
            'Контактная информация', {
                'fields': (
                    'phone_number',
                    'email',
                    'whatsapp',
                    'telegram'
                )
            })
    )
