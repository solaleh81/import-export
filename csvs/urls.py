from django.contrib import admin
from django.urls import path

from . import views
from .views import upload_file_view
app_name = 'csvs'

urlpatterns = [
    path('', views.upload_file_view, name='upload-file'),
]