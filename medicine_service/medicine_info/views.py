from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Item, Supplier, Type
from .serializers import ItemSerializer


@api_view(["POST"])
def create(request):
    serializer = ItemSerializer(data=request.data)
    try:
        Supplier.objects.get(id=request.data.get("supplier"))
    except:
        return Response(
            {"res": "Supplier with id does not exists"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    try:
        Type.objects.get(id=request.data.get("type"))
    except:
        return Response(
            {"res": "Type with id does not exists"},
            status=status.HTTP_400_BAD_REQUEST,
        )
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def get_all(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def get_detail(request, id):
    try:
        item_instance = Item.objects.get(id=id)
    except:
        return Response(
            {"res": "Patient with id does not exists"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    serializer = ItemSerializer(item_instance)
    return Response(serializer.data, status=status.HTTP_200_OK)