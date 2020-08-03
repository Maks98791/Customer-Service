from django.urls import path, include
from api import views


urlpatterns = [
    path('', views.customer_list),
    path('api/customers/', views.customer_list),
    path('api/customers/<pk>/', views.customer_details),
    path('api/customers/age/<age>', views.customer_list_by_age),
]