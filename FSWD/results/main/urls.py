from django.contrib import admin
from django.urls import include, path

from.import views

urlpatterns = [
    path('index',views.index),
    path('ccycle',views.ccycle),
    path('pcycle',views.pcycle),
    path('sem3',views.sem3),
    path('sem4',views.sem4),
    path('sem5',views.sem5),
    path('sem6',views.sem6),
    path('chs_branc',views.chs_branc),
    path('chs_branc/sem7a',views.sem7a),
    path('chs_branc/sem7b',views.sem7b),
    path('sem8',views.sem8),
]