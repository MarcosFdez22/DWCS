from django.urls import path
from . import views

urlpatterns = [
    path('', views.LoginView.as_view()), 
    path('thank_you/', views.thank_you, name='thank_you')

    
]
