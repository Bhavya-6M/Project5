from django.urls import path
from app1 import views

app_name='app2'

urlpatterns=[
    path('second/', views.first, name = 'second')
]