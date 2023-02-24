from django.urls import path,include
from django.contrib import admin
from exam import views
from django.contrib.auth.views import LogoutView
urlpatterns = [


    path('',views.home_view,name=''),
    path('logout', LogoutView.as_view(template_name='exam/logout.html'),name='logout'),

]

    