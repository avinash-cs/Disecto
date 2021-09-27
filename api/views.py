from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers,status
from disecto.models import Products,Orders,Invoice
from .serializers import InvoiceSerializer,OrdersSerializer,InvoicesSerializer
@api_view(['GET','PUT','DELETE'])
def invoice_detail(request,pk):
    try:
        orders = Invoice.objects.get(id=pk)
        # print(invoice)
    except Products.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)        
    if request.method == 'GET':
        serializer = InvoicesSerializer(orders)
        # print(serializer)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = InvoicesSerializer(orders, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)     
    elif request.Method == 'DELETE':
        orders.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','POST'])
def invoice_list(request):
    if request.method =='GET':
        invoices = Invoice.objects.all()
        serializer = InvoicesSerializer(invoices, many=True)
        return Response(serializer.data)
    elif request.method=="POST":
        serializer = InvoicesSerializer(data = request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_NOT_FOUND)

@api_view(['GET','POST'])
def product_list(request):
    if request.method =='GET':
        invoices = Products.objects.all()
        serializer = InvoiceSerializer(invoices, many=True)
        return Response(serializer.data)
    elif request.method=="POST":
        serializer = InvoiceSerializer(data = request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_NOT_FOUND)

@api_view(['GET','POST'])
def order_list(request):
    if request.method =='GET':
        orders = Orders.objects.all()
        serializer = OrdersSerializer(orders, many=True)
        return Response(serializer.data)
    elif request.method=="POST":
        serializer = OrdersSerializer(data = request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_NOT_FOUND)    
@api_view(['GET','PUT','DELETE'])
def order_detail(request,pk):
    try:
        orders = Orders.objects.get(id=pk)
        # print(invoice)
    except Products.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)        
    if request.method == 'GET':
        serializer = OrdersSerializer(orders)
        # print(serializer)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = OrdersSerializer(orders, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)     
    elif request.Method == 'DELETE':
        orders.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','PUT','DELETE'])
def product_detail(request,pk):
    try:
        invoice = Products.objects.get(id=pk)
        # print(invoice)
    except Products.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)        
    if request.method == 'GET':
        serializer = InvoiceSerializer(invoice)
        # print(serializer)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = InvoiceSerializer(invoice, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)     
    elif request.Method == 'DELETE':
        invoice.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)