from .serializer import VendorsSerializer, PurchaseSerializer
from .models import Vendors, PurchaseOrder
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def home(request):
    vender_obj = PurchaseOrder.objects.all()
    serialized_obj = PurchaseSerializer(vender_obj, many=True, validate=False)
    return Response(serialized_obj.data)

@api_view(['POST'])
def post_data(request):
    post_serializer = VendorsSerializer(data=request.data)
    if post_serializer.is_valid():
        post_serializer.save()
    return Response(post_serializer.data)


@api_view(['PUT'])
def home(request):
    vender_obj = Vendors.objects.all()
    serialized_obj = VendorsSerializer(vender_obj, many=True)
    return Response(serialized_obj.data)

@api_view(['DELETE'])
def home(request):
    vender_obj = Vendors.objects.all()
    serialized_obj = VendorsSerializer(vender_obj, many=True)
    return Response(serialized_obj.data)

