from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('form/', views.form_page, name='form'),
    path('result/', views.result_page, name='result'),
]
