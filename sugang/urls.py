from django.urls import path
from sugang import views

app_name = 'sugang'
urlpatterns = [
    
    path('', views.SubjectLV.as_view(), name='index'),
    
    path('subject', views.SubjectLV.as_view(), name='subject_list'),
    
    path('subject/<int:pk>/', views.SubjectDV.as_view(), name='subject_detail'),
    
    path('sign/<int:pk>/', views.SignDV.as_view(), name='sign_detail'),

    # Example: /photo/album/add/
    path('subject/add/', views.SubjectSignCV.as_view(), name='subject_add'),
    # Example: /photo/album/change/
    path('subject/change/', views.SubjectChangeLV.as_view(), name='subject_change'),
    # Example: /photo/album/99/update/
    path('subject/<int:pk>/update/', views.SubjectSignUV.as_view(), name='subject_update'),
    # Example: /photo/album/99/delete/
    path('subject/<int:pk>/delete/', views.SubjectDelV.as_view(), name='subject_delete'),
    # Example: /photo/photo/add/
    path('sign/add/', views.SignCV.as_view(), name='sign_add'),
    # Example: /photo/photo/change/
    path('sign/change/', views.SignChangeLV.as_view(), name='sign_change'),
    # Example: /photo/photo/99/update/
    path('sign/<int:pk>/update/', views.SignUV.as_view(), name='sign_update'),
    # Example: /photo/photo/99/delete/
    path('sign/<int:pk>/delete/', views.SignDelV.as_view(), name='sign_delete'),
]