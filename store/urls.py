from django.contrib import admin
from django.urls import path

from .views import home, login, signup, cart, checkout

urlpatterns = [
    path('', home.Index.as_view(), name="homepage"),
    path('signup',signup.Signup.as_view(), name="signup"),
    path('login',login.Login.as_view(), name="login"),
    path('logout',login.logout, name="logout"),
    path('cart',cart.Cart.as_view(), name="cart"),
    path('check-out',checkout.CheckOut.as_view(), name="checkout")
]