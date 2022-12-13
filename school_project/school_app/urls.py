from django.urls import path
from . import views 

app_name = 'school_app'

urlpatterns = [
    path(route='', view=views.index, name='index')
]