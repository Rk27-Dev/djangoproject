"""authproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,include
from app.views import home_view,java_view,python_view,datascince_view,logout_view,sign_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',view=home_view),
path(r'java/',view=java_view),
path(r'python',view=python_view),
path(r'datascince/',view=datascince_view),
path(r'logout/',view=logout_view),
path(r'signup/',view=sign_view),
path(r'accounts/',include('django.contrib.auth.urls')),
]
