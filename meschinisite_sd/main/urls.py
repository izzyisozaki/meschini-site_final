from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path("contatti/", views.contatti, name="contatti"),
    path("chisiamo/", views.chisiamo, name="chisiamo"),
    path("offertelavoro/", views.offerte_lavoro, name="offerte_lavoro"),
    path("areaziende/", views.area_aziende, name="area_aziende"),
    path("register/", views.register, name="register"),
    path("login/", views.login_view, name="login"),    # Usa views.login_view
    path("logout/", views.logout_view, name="logout"), # Usa views.logout_view
    path("area_riservata/", views.area_riservata, name="area_riservata"),

]

