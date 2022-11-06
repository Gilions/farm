from django.contrib import admin
from django.utils.html import format_html

from apps.product.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_active', 'created_at', 'updated_at', 'image_tag', )
    list_display_links = ('name', 'image_tag', )
    list_editable = ('price', 'is_active', )
    list_filter = ('is_active', )
    search_fields = ('name', )

    def image_tag(self, obj):
        return format_html('<img src="{}" style="max-width:100px; max-height:100px"/>'.format(obj.image.url))

    image_tag.short_description = 'Фотография'


