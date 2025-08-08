from django.urls import path
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

    path('create_order/', views.createOrder, name="create_order"),
    path('edit_order/<str:product_id>/', views.editOrder, name="edit_order"), # Not quite sure what I should do here. This path is called by inventory.html
    path('update_order/<str:pk>/', views.updateOrder, name="update_order"),
    path('delete_order/<str:pk>/', views.deleteOrder, name='delete_order'),


]

