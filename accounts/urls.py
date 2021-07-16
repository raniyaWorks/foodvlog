from django.urls import path
from . import views

urlpatterns=[
    path('hlo',views.hlo,name='hlo')
]