from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),

    path('', views.landing, name='landing'),
    path('landing/', views.landing, name='landing'),
    path('home/', views.home, name='home'),
    path('dashboard/<str:pk>/', views.dashboard, name='dashboard'),
    path('inventory/', views.inventory, name='inventory'),
    path('user/', views.userPage, name='user-page'),
    path('account/', views.accountSettings, name='account'),


    path('edit_order/<str:product_id>/', views.editOrder, name="edit_order"), 
    path('create_order/<str:pk>/', views.createOrder, name="create_order"),
    path('update_order/<str:pk>/', views.updateOrder, name="update_order"),
    path('delete_order/<str:pk>/', views.deleteOrder, name='delete_order'),

    path('reset_password/', auth_views.PasswordResetView.as_view(), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset_password_completed/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),

]

