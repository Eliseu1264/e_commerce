
from django.contrib import admin
from django.urls import path
from .view import hoje_page

urlpatterns = [
    path('', hoje_page),
    path('admin/', admin.site.urls),
]
