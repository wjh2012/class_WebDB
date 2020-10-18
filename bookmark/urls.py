from django.urls import path, re_path
from bookmark import views

app_name = 'bookmark'
urlpatterns = [
    path('', views.BookmarkLV.as_view(), name='index'),
    path('<int:pk>/', views.BookmarkDV.as_view(), name='detail'),
    path('search/', views.SearchFormView.as_view(), name='search'),
]