from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('delete_sub/<sub_id>', views.delete_sub, name ='delete-sub'),
    path('send_update/<sub_id>', views.send_update, name='send-update'),
]