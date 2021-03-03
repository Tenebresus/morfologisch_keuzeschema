from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Category


class KeuzeSchemaView(TemplateView):
    template_name = "keuzeschema.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()

        return context
