from django.urls import path

from apps.product.views import IndexView, DetailCardView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<uuid:guid>', DetailCardView.as_view(), name='card_view')
]
