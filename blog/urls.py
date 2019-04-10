from django.urls import path
from .import views

urlpatterns =[
    path('blogs',views.allblogs,name='allblogs'),
    path('blogs/<int:blog_id>/', views.blog_detail, name ='blogdetail'),
    path('index',views.index,name='index'),
]
