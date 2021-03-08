from django.core.serializers import serialize
from django.db.models import Value
from django.db.models import CharField
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, View
from .models import Product, Category, Leverancier
import json

class KeuzeSchemaView(TemplateView):
    template_name = "keuzeschema.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()

        return context

class ProductView(View):
    def get(self, request, sub_category):
        products = Product.objects.filter(sub_category__sub_category=sub_category).values('leverancier_id__leverancier', 'productnr', 'type',
                                                                                          'vermogen', 'belasting', 'rendement').all()
        # data = serialize('python', products)
        return JsonResponse(list(products), safe=False)