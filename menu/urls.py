from django.urls import path

from . import views
urlpatterns = [
    path('', views.suck),
    path('logout', views.logout_click),
    path('add_adm', views.add_adm),
    path('add_user', views.add_user),
    path('delete_admin', views.delete_admin),
    path('delete_user', views.delete_user),
]