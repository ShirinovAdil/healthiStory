from django.urls import path, include
from . import views

urlpatterns = [
    path('register', views.user_register, name="register"),
    path('login', views.user_login, name="login"),
    path('logout', views.user_logout, name="logout"),

    path('ajax/load-cities', views.load_cities, name='ajax_load_cities'),
    path('ajax/load-districts/', views.load_districts, name='ajax_load_districts'),  # <-- this one here

]
