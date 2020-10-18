from django.urls import path, re_path
from namecard import views

app_name = 'namecard'
urlpatterns = [
    path('', views.NamecardLV.as_view(),name='index'),
    path('<int:pk>/', views.NamecardDV.as_view(), name='detail'),
    path('search/', views.SearchFormView.as_view(), name='search'),
]