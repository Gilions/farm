from django.urls import path

from apps.product.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]
