from django.urls import path
from . import views

app_name = 'notes'

urlpatterns = [
    path('add/',views.add_notes_view,name='add'),
    path('show_notes/',views.show_notes_view,name='show_notes')
]