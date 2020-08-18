from django.conf.urls import url
from django.contrib import admin
from . import views
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'trial$', views.trial)
]