from  django.urls import path
from . import views

urlpatterns =[
    path('', views.index , name='list'),
    path('update/<str:pk>/', views.upadateTask, name='update'),
    path('delete/<str:pk>/', views.delete , name='delete'),
]
