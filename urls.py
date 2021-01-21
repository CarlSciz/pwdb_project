from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('wrestler/<int:wrestler_id>', views.wrestler_by_id, name='wrestler_by_id'),
]