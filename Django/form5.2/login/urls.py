from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'), 
    path('thank_you/', views.thank_you, name='thank_you')

    
]
