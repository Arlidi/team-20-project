from django.urls import path, include
from new.views import *


app_name = 'new'
urlpatterns = [
    path('create/', camera_Create_View.as_view()),
    path('all/', camera_list_view.as_view()),
    path('deteil/<int:pk>', camera_deteil_view.as_view())
]
