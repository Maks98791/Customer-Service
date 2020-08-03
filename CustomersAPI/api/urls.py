from django.urls import path, include
from api import views


urlpatterns = [
    path('customers/', views.customer_list),
    path('customers/<pk>/', views.customer_details),
    path('customers/age/<age>', views.customer_list_by_age),
]