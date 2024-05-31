from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from medicine_info.models import Item
from medicine_info.serializers import ItemSerializer

@api_view(["PUT"])
def update(request, id):
    try:
        medicine = Item.objects.get(id=id)
    except:
        return Response(
            {"res": "Object with medicine id does not exists"},
            status=status.HTTP_400_BAD_REQUEST,
        )
    serializer = ItemSerializer(instance=medicine, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["PUT"])
def update_quantity(request, id):
    try:
        medicine = Item.objects.get(id=id)
    except:
        return Response(
            {"res": "Object with medicine id does not exists"},
            status=status.HTTP_404_NOT_FOUND,
        )
    if (medicine.quantity < request.data.get("quantity", 0)):
        return Response(
            {"res": "Object with medicine id does not exists"},
            status=status.HTTP_400_BAD_REQUEST,
        )
    quantity = medicine.quantity - request.data.get("quantity", 0)
    medicine.quantity = quantity
    medicine.save()
    return Response({"res": "Update quantity successfull"}, status=status.HTTP_200_OK)

@api_view(["DELETE"])
def delete(id, *args, **kwargs):
    try:
        medicine = Item.objects.get(id=id)
    except:
        return Response(
            {"res": "Object with medicine id does not exists"},
            status=status.HTTP_400_BAD_REQUEST,
        )
    medicine.delete()
    return Response({"res": "Object deleted!"}, status=status.HTTP_200_OK)