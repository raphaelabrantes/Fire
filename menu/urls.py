from django.urls import path

from . import views
urlpatterns = [
    path('', views.suck),
    path('logout', views.logout_click),
    path('add_adm', views.add_adm),

]