from django.urls import path
from Home import views

app_name = "Home"

urlpatterns = [
    path("",views.index, name="index"),
    # path("menu/",views.menu, name="menu"),
    path("about/",views.about, name="about"),
    path("contact/",views.contact, name="contact"),
    path("register/",views.register, name="register"),
    path("login/",views.login, name="login"),
    path("logout/",views.logout, name="logout"),
    path("profile/",views.profile, name="profile"),
]