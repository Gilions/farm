from django.views.generic import ListView, DetailView, TemplateView

from apps.misc.models import SiteSettings
from apps.product.models import Product
from conf.settings import PAGINATOR_SIZE


class IndexView(ListView):
    model: Product = Product
    template_name: str = 'index.html'
    context_object_name: str = 'products'
    paginate_by: int = PAGINATOR_SIZE

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['info'] = SiteSettings.get_solo()
        return context

    def get_queryset(self):
        return Product.objects.filter(is_active=True)


class DetailCardView(DetailView):
    model: Product = Product
    template_name: str = 'detail_card.html'
    pk_url_kwarg: str = 'guid'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['info'] = SiteSettings.get_solo()
        return context
