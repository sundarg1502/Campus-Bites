from django.urls import path
from Home import views

app_name = "Home"

urlpatterns = [
    path("",views.index, name="index"),
    path("menu/",views.menu, name="menu"),
]