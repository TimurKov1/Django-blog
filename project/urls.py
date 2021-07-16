from project import views as v
from django.urls import path

urlpatterns = [
    path('', v.HomeShow.as_view(), name='home'),
    path('posts/', v.BlogShow.as_view(), name='blog'),
    path('posts/<int:pk>', v.DetailShow.as_view(), name='postdetails'),
]