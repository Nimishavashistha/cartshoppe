from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

from .views import home, login, signup, cart, checkout, orders

urlpatterns = [
    path('', home.Index.as_view(), name="homepage"),
    path('signup',signup.Signup.as_view(), name="signup"),
    path('login',login.Login.as_view(), name="login"),
    path('logout',login.logout, name="logout"),
    path('productDetail/<int:pk>/',home.ProductDetailView.as_view(), name="productDetail"),
    path('cart',cart.Cart.as_view(), name="cart"),
    path('check-out',checkout.CheckOut.as_view(), name="checkout"),
    path('orders',orders.OrderView.as_view(), name="orders"),
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name="password_reset.html"),name="password_reset"),
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name="password_reset_done.html"),name="password_reset_done"),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"),name="password_reset_confirm"),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"),name="password_reset_complete")
]