from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', get_home, name='home'),
    path('catalog/', ProductView.as_view(), name='catalog'),
    path('contact/', get_contact, name='contact'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('verify/<int:user_pk>/<str:token>/', VerifyEmailView.as_view(), name='verify'),
    path('products/<int:category_id>/', product_list, name='product_list'),
]
