from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404, handler500

from conf import settings


handler404 = 'apps.misc.views.page_not_found'
handler500 = 'apps.misc.views.server_error'

urlpatterns = [
    path('dashboard/', admin.site.urls),
    path('about/', include('apps.about.urls')),
    path('', include('apps.product.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
