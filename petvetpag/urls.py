from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('porhacer/', views.porhacer, name='porhacer'),
    path('tienda/', views.tienda, name='tienda'),

    #crud para tienda  
    path('tienda/create/', views.product_create, name='product_create'),
    path('tienda/update/<int:id>/', views.product_update, name='product_update'),
    path('tienda/delete/<int:id>/', views.product_delete, name='product_delete'),

]
