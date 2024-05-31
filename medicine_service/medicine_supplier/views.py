from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from medicine_info.models import Supplier
from medicine_info.serializers import SupplierSerializer


# Create your views here.
@api_view(["POST"])
# @permission_classes([IsAuthenticated])
def create(request):
    serializer = SupplierSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["PUT"])
# @permission_classes([IsAuthenticated])
def update(request, id):
    try:
        status = Supplier.objects.get(id=id)
    except:
        return Response(
            {"res": "Supplier with id does not exists"},
            status=status.HTTP_400_BAD_REQUEST,
        )
    serializer = SupplierSerializer(instance=status, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def get_all(request):
    list_status = Supplier.objects.all()
    serializer = SupplierSerializer(list_status, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
