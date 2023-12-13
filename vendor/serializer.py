from .models import Vendors, PurchaseOrder
from rest_framework import serializers

class VendorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendors
        fields = "__all__"
        
class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = "__all__"
        