from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('add/', views.add_post_view, name='add_post'),
    path('delete/<int:post_id>/', views.delete_post_view, name='delete_post'),
]