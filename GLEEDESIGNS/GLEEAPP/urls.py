from django.conf import settings
from django.conf.urls.static import static
from  django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home-page'),
    path('index2/',views.index2,name="index2"),
    path('controller/', views.controller, name="controller "),
    path('IMAGES/upload/', views.uploadIMAGES, name='upload_IMAGES'),
    path('IMAGES/', views.IMAGESList, name='IMAGES_list'),
    path('IMAGES/<int:pk>', views.deleteIMAGES, name='IMAGES'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
