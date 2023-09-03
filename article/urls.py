from django.contrib import admin
from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    
    path('article/<int:article_id>/', views.article_detail, name='article_detail'),
    path('software/', views.software, name='software'),
    path('math/',views.math, name='math'),
    path('dashboard/',views.dashboard,name="dashboard"),
    path('addarticle/',views.addArticle,name='addArticle')
    
    
    
    
    
]