from django.contrib import admin
from django.urls import path,include
from django.urls import path
from manager import views
from django.contrib.auth.views import LoginView


urlpatterns = [
path('home',views.ManagerHomeView.as_view(),name="manager_home"),
# path('login/', LoginView.as_view(template_name='managerlogin.html'), name='login'),
    path('login/',views.login_view, name="manager_login"),
    path('purchase',views.PurchaseView.as_view(),name="manager_purchase"),
    path('stock',views.StockView.as_view(),name="med_stock"),
    path('orders',views.order_list,name="order_details"),




]
