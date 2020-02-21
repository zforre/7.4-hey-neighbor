from django.urls import path

from . import views

app_name= 'tools'

urlpatterns = [
    path('myitems/', views.ListView.as_view(), name='myitems'),
    path('userlist/', views.UserView.as_view(), name='userlist'),
    path('', views.IndexView.as_view(), name='index')
]