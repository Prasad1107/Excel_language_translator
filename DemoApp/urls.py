from django.urls import re_path
from django.contrib import admin
from . import views
from django.conf import settings

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^$', views.index),
    re_path(r'trial$', views.trial)
]