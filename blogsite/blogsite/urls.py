"""
URL configuration for blogsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, re_path, include

from .views import (
    home_page,
    temp_page,
    about_page,
    re_page
    )

from blog.views import (
    blog_list_view,
    blog_post_details
    )

urlpatterns = [
    path('my-admin/', admin.site.urls),
    path('', home_page),

    # example path for template page
    path('home', temp_page),
    path('about', about_page),

    # example page for regression path
    re_path(r'^pages?/$', re_page),

    # app views path
    path('blogpost/', include('blog.urls')),
]
