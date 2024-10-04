from django.urls import path
from .views import home, register, login_view 
from musicindex import views

urlpatterns = [
    path('', home, name='home'),
    path('home/',views.home,name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
]
