from django.urls import path
from . import views
from .views import edit_all_info , delete_info

urlpatterns = [
    path('', views.index, name='index'),
    path('all_info/', views.all_info, name ='all_info'),
    path('create-info/', views.create_all_info, name='create_all_info'),  
    path('edit_all_info/<int:id>/', edit_all_info, name='edit_all_info'),
    path('delete_info/<int:id>/', delete_info, name='delete_info'),

]