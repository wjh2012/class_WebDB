from django.urls import path, re_path
from student import views

app_name = 'student'
urlpatterns = [
    path('', views.StudentLV.as_view(),name='index'),
    path('<int:pk>/', views.StudentDV.as_view(), name='detail'),
    path('search/', views.SearchFormView.as_view(), name='search'),
]