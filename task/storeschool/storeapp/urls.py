
from django.urls import path
from . import views

app_name = 'storeapp'

urlpatterns = [
    path('',views.home,name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('regform/', views.regform, name='regform'),
    path('ajax/load-courses/', views.load_courses, name='ajax_load_courses'),  # AJAX

]
