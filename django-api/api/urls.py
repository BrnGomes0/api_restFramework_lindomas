from django.urls import path
from . import views

urlpatterns = [
    path('clientes', views.client_list),
    path('users', views.ClientView.as_view()),
    path('usuario/<int:pk>',views.ClientDetailView.as_view())
]
