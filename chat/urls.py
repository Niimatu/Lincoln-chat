from django.urls import path
from . import views 

app_name = 'chat'

urlpatterns = [
    path('', views.ChatListView.as_view(), name='all'),
    path('new/', views.ChatCreateView.as_view(), name='new'),
    
]
