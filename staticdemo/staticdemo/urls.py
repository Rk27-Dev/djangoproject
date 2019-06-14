"""staticdemo URL Configuration

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
from django.urls import path
from app.views import home,staticview,registerview,display,cont,session_view,name_view,age_view,gf_view,result_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'home/',view=home),
    path(r'staticview/',view=staticview),
    path(r'regi/',view=registerview),
    path(r'display/',view=display),
    path(r'cont/',view=cont),
    path(r'session/',view=session_view),
    path(r'name/',view=name_view),
    path(r'age/',view=age_view),
    path(r'gf/',view=gf_view),
    path(r'result/',view=result_view)
]



