"""curd_cl URL Configuration

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
from app.views import home_view,create_view,list_view,details_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'',view=home_view.as_view()),
    path(r'list/',view=list_view.as_view()),
    path(r'^(?P<pk>/d+)/',view=details_view.as_view(),name='details'),
    path(r'create/',view=create_view.as_view()),
    path(r'^update/(?P<pk>/d+)/',view=details_view.as_view())
]
