from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('', views.obtener_info_cliente, name='obtener_info_cliente'),

]
