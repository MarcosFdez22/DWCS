from django.urls import path
from . import views


urlpatterns = [
    path("", views.StudentFormView.as_view()),
    path("thank_you",views.thank_you),
    path("list",views.StudentList.as_view(), name="list"),
    path('student/<int:pk>/edit/', views.StudentUpdateView.as_view(), name='student_update'),
    path('student/<int:pk>/delete/', views.StudentDeleteView.as_view(), name='student_delete')
    
    
]
