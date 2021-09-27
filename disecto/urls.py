from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from .views import *
from api.views import *
app_name = 'disecto'
urlpatterns = [
    path('', index, name = "Home"),
    path('disecto/productlist/', productlist, name="productlist"),
   
    path('disecto/buyproduct/', buyproduct, name="buyproduct"),
    path('disecto/addproducts/', addproducts, name="addproducts"),
    path('disecto/updateproduct/<str:pk>',updateproduct, name="updateproduct"),
    path('disecto/deleteproduct/<str:pk>', deleteproduct, name="deleteproduct"), 
    path('disecto/orders/', orders, name="orders"),
    path('disecto/updateorders/<str:pk>', updateorders, name="updateorders"),
    path('disecto/deleteorders/<str:pk>', deleteorders, name="deleteorders"), 
   
    path('invoice/', InvoiceListView.as_view(), name="invoice-list"),
    path('create/', createInvoice, name="invoice-create"),
    path('invoice-detail/<id>', view_PDF, name='invoice-detail'),
    path('invoice-download/<id>', generate_PDF, name='invoice-download'),
    #api
    path('api/products/',product_list,name='product_list'),
    path('api/orders/',order_list,name='order_list'),
    path('api/products/<int:pk>',product_detail,name='product_detail'),
    path('api/orders/<int:pk>',order_detail,name='order_list'),
    path('api/invoices/',invoice_list,name='invoice_list'),
    path('api/invoices/<int:pk>',invoice_detail,name='invoice_detail'),

]
