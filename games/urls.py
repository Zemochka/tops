from django.urls import path
from . import views

urlpatterns= [
    path('', views.home, name="home"),
    path('codenames', views.codenames, name="codenames"),
    path('pandemic', views.pandemic, name="pandemic"),
    path('spyfall', views.spyfall, name="spyfall"),
    path('celestia', views.celestia, name="celestia"),
    path('citadels', views.citadels, name="citadels"),
    path('stupid-casual', views.stupidCasual, name="stupidCasual"),
    path('ticket-to-ride', views.ticketToRide, name="TtR"),
    path('exploding-kittens', views.cats, name="cats"),
    path('plunking-pairs', views.plunkingPairs, name="pluckingPairs")
]