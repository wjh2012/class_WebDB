from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include
from mysite.views import HomeView
from mysite.views import HomeView, UserCreateView, UserCreateDoneTV

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', UserCreateView.as_view(), name='register'),
    path('accounts/register/done/', UserCreateDoneTV.as_view(), name='register_done'),

    path('',HomeView.as_view(), name = 'home'),    
    path('bookmark/', include('bookmark.urls')),
    path('blog/', include('blog.urls')),
    path('namecard/', include('namecard.urls')),
    path('student/', include('student.urls')),
    path('photo/', include('photo.urls')),
    path('sugang/', include('sugang.urls')),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
