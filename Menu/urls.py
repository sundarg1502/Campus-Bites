from django.urls import path
from Menu import views

app_name = "Menu"

urlpatterns = [
    path("",views.index,name='index'),
    path("/cart",views.cart,name='cart')
]