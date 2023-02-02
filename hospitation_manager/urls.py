from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('appeal_responses/', views.appeal_responses_index),
    path('appeal_responses/details/<int:id>', views.appeal_responses_details)
]