from django.urls import path

from . import views
urlpatterns = [
    path("",views.home,name="home"),
    path("register",views.registration,name="register"),
    path("login/",views.login,name="login"),
    path("checklogin",views.checklogin,name="checklogin"),
    path("about",views.about,name="about"),
    path("contact",views.contact_us,name="contact"),
    path('zodiacsign/', views.zodiacsign, name='zodiacsign'),
    path('changepassword/', views.changepassword, name='changepassword'),
    path('updatepassword',views.updatepwd,name='updatepassword'),

    path('horoscope/', views.horoscope, name='horoscope'),



    ]
