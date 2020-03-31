from accounts import views
from django.urls import path

urlpatterns = [
path('login/', views.login_view, name = 'login'),
path('signup/', views.signup_view, name = 'signup'),
path('register_success/', views.success_view, name = 'register_success')
]