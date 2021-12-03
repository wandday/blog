from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('single_post/<str:pk>', views.single_post, name='single_post'),

]