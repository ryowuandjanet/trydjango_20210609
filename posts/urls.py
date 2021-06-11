from django.urls import path
from .views import *

app_name="posts"

urlpatterns = [
  path('', post_list,name="list"),
  path('<str:slug>/', post_detail,name="detail"),
  path('create', post_create,name="create"),
  path('<str:slug>/edit/', post_update,name="update"),
  path('<str:slug>/delete/', post_delete,name="delete"),
]
