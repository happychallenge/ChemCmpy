from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^vendors/$', views.vendor_list, name='vendor_list'),
    url(r'^vendors/(?P<id>\d+)$', views.vendor_detail, name='vendor_detail'),

    url(r'^proudct/$', views.product_list, name='product_list'),
    url(r'^proudcts/(?P<id>\d+)$', views.product_detail, name='product_detail'),


]
