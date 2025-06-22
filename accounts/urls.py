

from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name='dashboard'),
    path("registration/", views.registration, name='registration'),
    path("signin/", views.signin, name='signin'),
    path('logout/', views.signout, name='logout'),
    path("dashboard", views.dashboard, name='dashboard'),
]

# urlpatterns = [
#     path('', views.signin, name='signin'),
#     path('dashboard/', views.dashboard, name='dashboard'),
#     path('registration/', views.registration, name='registration'),
#     path('signout/', views.signout, name='signout'),
# ]