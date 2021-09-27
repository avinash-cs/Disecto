from django.db.models import fields
from rest_framework import serializers
from disecto.models import Products,Orders,Invoice,LineItem

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Products
        fields= ('id','name','description','price','quantity_avail')

class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ('id','product','quantity')

class LineItemSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('__all__')
        
class  InvoicesSerializer(serializers.ModelSerializer):
    entry = LineItemSerializer(many=True,read_only=True)
    class Meta:
        model = Invoice
        fields = ('id','customer','customer_email','billing_address','date','total_amount','entry')
