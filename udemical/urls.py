
from django.contrib import admin
from django.urls import path,include
from article import views
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name="index"),
    path('articles/', include('article.urls', 'articles')),
    path('user/',include('user.urls','user')),
    path('about/', views.about, name="about"),
    path('contact/',views.contact, name="contact" )
]