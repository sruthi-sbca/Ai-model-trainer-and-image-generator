from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_gallery, name='upload_gallery'),
    path('', views.view_gallery, name='view_gallery'),
]
