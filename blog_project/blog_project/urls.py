"""blog_project URL Configuration

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
from django.urls import path, re_path
from blog.views import post_view,post_details_view,email_send_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'',view=post_view),
    # path(r"",view=Postlist_view.as_view()),
    re_path(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$',view=post_details_view,name='post_details'),
    # path(r'post_details/',view=post_details_view),
    re_path(r'^(?P<id>\d+)/share/$',view=email_send_view)
]
