from django.urls import path
from . import views

urlpatterns=[
    path("profile",views.profile_view,name="profile"),
    path("account/signup/", views.CustomSignupView.as_view(), name="account_signup"),
    path('', views.restaurant_homepage, name='homepage'),
]
