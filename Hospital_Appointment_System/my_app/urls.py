from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('appointment/add/', views.AppointmentCreate.as_view(), name='appointment_create'),
    path('appointment/<int:pk>/edit/', views.AppointmentUpdate.as_view(), name='appointment_update'),
    path('appointment/<int:pk>/delete/',views.AppointmentDelete.as_view(), name='appointment_delete'),
    path('logout/', LogoutView.as_view(), name='logout'),

]
