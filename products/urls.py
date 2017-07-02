from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^vendors/$', views.vendor_list, name='vendor_list'),
    url(r'^vendors/(?P<id>\d+)/$', views.vendor_detail, name='vendor_detail'),
    url(r'^vendors/add/$', views.vendor_add, name='vendor_add'),
    url(r'^vendors/update/(?P<id>\d+)/$', views.vendor_update, name='vendor_update'),

    url(r'^proudct/$', views.product_list, name='product_list'),
    url(r'^proudcts/(?P<id>\d+)/$', views.product_detail, name='product_detail'),

    url(r'^contact/$', views.contact_list, name='contact_list'),
    url(r'^contact/add/$', views.contact_add, name='contact_add'),
    url(r'^contact/update/(?P<id>\d+)/$', views.contact_update, name='contact_update'),

]
