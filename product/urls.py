from django.urls import re_path, path
from . import views

urlpatterns = [
    re_path(r'^$', views.list_products_view, name='products'),
    path('category/<str:category_code>', views.categorized, name='categorized'),
    path('<str:product_code>', views.single_product_view, name='single_product'),
]
