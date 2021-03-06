from django.shortcuts import render
from django.views.generic.base import TemplateView

class HomePageView(TemplateView):

    template_name = "ships/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author_name'] = 'Javier'
        context['author_url'] = 'https://github.com/Javierb'
        return context

