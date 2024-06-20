from django.urls import path
from . import views
from .views import ProductListView, ProductDetailView

app_name = 'store'

urlpatterns = [
  path('product_list', ProductListView.as_view(), name='product_list'),
  path('product_detail/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
  # path('product_buy/<int:id>', views.ProductBuy, name='product_buy')
]