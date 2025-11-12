from . import views

from django.urls import path


app_name = 'shop'

urlpatterns = [
    path("download/", views.download_pdf, name='download'),
    path("", views.index, name='index')
]
