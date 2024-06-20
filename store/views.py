from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from .models import Product, CartItem

# Create your views here.

class ProductListView(ListView):
    model = Product
    template_name = 'store/product_list.html'

    def get_queryset(self):
        queryset = super(ProductListView, self).get_queryset()
        product_name = self.request.GET.get('product_name')
        if product_name:
          queryset = queryset.filter(product_type__name = product_name)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['product_name'] = self.request.GET.get('product_name') or ''
        return context

class ProductDetailView(DetailView):
    model = Product
    template_name = 'store/product_detail.html'

# class CartItemCreateView(CreateView):
#     model = CartItem
#     template_name = 'store/.html'

