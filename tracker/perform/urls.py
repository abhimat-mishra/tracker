from django.urls import path
from . import views

app_name = 'tracker'

urlpatterns = [
    path('home/',views.home_view,name='home'),
    path('show/',views.show_view,name='show'),
    path('delete_tasks/<str:date>/', views.delete_tasks_view, name='delete_tasks'),
]