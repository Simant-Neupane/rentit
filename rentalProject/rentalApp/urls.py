from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',index,name='index'),
    path('about/',about,name='about'),
    path('forrent/',for_rent,name='for_rent'),
    path('forsale/',for_sale,name='for_sale'),
    path('services/',services,name='services'),
    path('contact/',contact,name='contact'),
    path('terms/',terms,name='terms'),
    path('privacy/',privacy,name='privacy'),
    path('details/<int:id>',rent_details,name="details"),
    path('uploadproperty/',upload_property,name="property"),
    path('myproperty/',my_property,name="myproperty"),
    path('myproperty/delete/<int:id>/',property_delete,name="propertydelete"),
    path('myproperty/edit/<int:id>/',property_edit,name="propertyedit"),


    
    path('register/',register,name='register'),
    path('login/',log_in,name='login'),
    path('logout/',log_out,name='logout'),
    path('profile/',profile,name='profile'),
    path('update_profile/',update_profile,name='updateprofile'),
    path('change_password/',change_password,name='change_password'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]