from django.urls import path
from .import views
urlpatterns = [
    path('',views.home,name='home'),
    path('hello/<str',views.hlo,name='hello'),
]
