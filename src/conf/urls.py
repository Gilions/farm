from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from conf import settings

urlpatterns = [
    path('dashboard/', admin.site.urls),
    path('', include('apps.product.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
