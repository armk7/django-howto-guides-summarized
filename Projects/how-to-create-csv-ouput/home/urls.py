from django.urls import path

from . import views

app_name = 'home'

urlpatterns = [
    path('download/csv-template-2/', views.template_csv_improved, name='template_csv2'),
    path('download/csv-template/', views.template_csv, name='template_csv'),
    path('download/large-csv/', views.stream_csv, name='stream_csv'),
    path('download/', views.download_csv, name='download_csv'),
    path('', views.index),
]