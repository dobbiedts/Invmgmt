from django.urls import path
from . import views

urlpatterns = [
   path('register/', views.register_request, name="register"),
   path('', views.home, name = "home"),
   path('add_invoice/', views.add_invoice, name = "add_invoice"),
   path ('list_invoice/', views.list_invoice, name = "list_invoice"),
   path('update_invoice/<str:pk>/', views.update_invoice, name = "update_invoice"),
   path('delete_invoice/<str:pk>/', views.delete_invoice, name = "delete_invoice"),
   path('login/', views.login_request, name="login"),
   path('logout/', views.logout_request, name= "logout"),
]

