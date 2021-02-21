"""dj_todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from registration import views


admin.site.site_title="MyTodo Admin site"
admin.site.site_heaader="MyTodo Admin site"
admin.site.index_title="Menu"
admin.site.register(User)
#admin.site.unregister(Group)


index_view = TemplateView.as_view(template_name="registration/index.html")

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("todo.urls")),
    path("", login_required(index_view), name="index"),
    path('', include("django.contrib.auth.urls")),
    path("account/", login_required(index_view), name="index"),
    path("signup/", views.SignUpView.as_view(), name="signup"),
]
