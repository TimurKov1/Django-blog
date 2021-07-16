
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as v
from django.conf.urls.static import static
from django.conf import settings
from user import views 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('project.urls')),
    path('registration/', views.registration, name='reg'),
    path('login/', v.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', v.LogoutView.as_view(template_name='user/logout.html'), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('updateprofile/', views.update_profile, name='updateprofile')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)