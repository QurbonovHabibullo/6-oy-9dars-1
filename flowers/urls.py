from django.urls import path
from . import views

urlpatterns = [
    path('', views.flower_list, name='flower_list'),
    path('category/<int:category_id>/', views.flowers_by_category, name='flowers_by_category'),
    path('flower/<int:flower_id>/', views.flower_detail, name='flower_detail'),
    path('add_flower/',views.add_flowers,name = 'add_flowers'),
]
