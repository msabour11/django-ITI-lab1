
from django.urls import path
from Amazon.views import hello,product,filter_products,product_list,product_detail

urlpatterns = [
    
    path('hello',hello, name='hello'),
    path('products',product, name='products'),
    path('filter/<id>',filter_products, name='filter_products'),
    path('',product_list, name='product_list'),
    path('product/<int:id>/', product_detail, name='product_detail'),





]
