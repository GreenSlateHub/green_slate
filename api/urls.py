from django.urls import path
from . import views
urlpatterns = [
    path('get-data', views.getData),
    path('add-data', views.addItem),
]
