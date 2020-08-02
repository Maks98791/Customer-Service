from django.conf.urls import url
from api import views


urlpatterns = [
    url(r'^customers/$', views.customer_list),
    url(r'^customers/(P&lt;pk&gt;[0-9]+)$', views.customer_details),
    url(r'^customers/age/(P&lt;age&gt;[0-9]+)/$', views.customer_list_by_age),
]