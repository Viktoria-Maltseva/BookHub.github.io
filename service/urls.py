"""
URL configuration for service project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from service import views
from django.conf.urls import include
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('', views.index),
    path('books/', include('books.urls')),
    path('authors/<int:author_id>/', views.author_show, name='author_show'),
    path('genres/<int:genre_id>/', views.show_info_genres, name='genre_show'),
    path('authors/<str:auth_str>/', views.notshowauth),
    path('genres/<str:auth_str>/', views.notshowauth),
    path('accounts/', include('django.contrib.auth.urls')),
    path('comments/', include('comments.urls')),
]
