from django.urls import re_path, path
from . import views

urlpatterns = [
    re_path(r'^$', views.list_products_view, name='products'),
    path('category/<str:cat_name>',views.categorized ,name='categorized'),
    path('<int:pk>',views.single_product_view ,name='single_product'),
]
