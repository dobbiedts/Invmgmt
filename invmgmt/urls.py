from django.urls import path
from . import views

urlpatterns = [
   path('', views.home, name = "home"),
   path('add_invoice/', views.add_invoice, name = "add_invoice"),
   path ('list_invoice/', views.list_invoice, name = "list_invoice"),
   path('update_invoice/<str:pk>/', views.update_invoice, name = "update_invoice"),
   path('delete_invoice/<str:pk>/', views.delete_invoice, name = "delete_invoice"),
]

