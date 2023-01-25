from django.urls import path

from laboratories.views import detail
from laboratories.views import update
from laboratories.views import index
from laboratories.views import create
from laboratories.views import delete

app_name = 'laboratories'

urlpatterns = [
    path('', index, name='index'),
    path('create', create, name='create'),
    path('<int:pk>', detail, name='detail'),
    path('<int:pk>/update', update, name='update'),
    path('<int:pk>/delete', delete, name='delete'),
]
