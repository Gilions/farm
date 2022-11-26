from django.views.generic import TemplateView

from apps.misc.models import SiteSettings


class AboutView(TemplateView):
    template_name: str = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['info'] = SiteSettings.get_solo()
        return context
