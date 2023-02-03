from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('appeal_responses/', views.appeal_responses_index),
    path('appeal_responses/details/<int:id>', views.appeal_responses_details),
    path('appeal_responses/edit/<int:id>', views.appeal_responses_edit),

    path('wzhz/', views.wzhz_index, name = 'wzhz_index'),
    path('wzhz/add', views.wzhz_add, name = 'add_wzhz_member'),
    path('wzhz/details/<int:wzhz_id>', views.wzhz_details),

    path('hospitation_planning/', views.hospitation_planning_index),
    path('hospitation_planning/details/<int:hospitation_id>', views.hospitation_planning_details),
    path('hospitation_planning/edit/<int:hospitation_id>', views.hospitation_planning_edit),
    path('hospitation_planning/add', views.hospitation_planning_add, name = 'add_hospitation'),
]


