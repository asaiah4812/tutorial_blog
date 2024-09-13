from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('post/<slug:slug>/', views.post, name='post'),
    path('post-delete/<str:pk>/', views.post_delete, name='post-delete'),
    path('update_post/<str:pk>/', views.update_post, name='update-post')
]
