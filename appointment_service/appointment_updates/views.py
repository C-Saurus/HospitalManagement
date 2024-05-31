from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from appointment_info.models import Item, Status, Type
from appointment_info.serializers import ItemSerializer

@api_view(["PUT"])
def update(request, id):
    try:
        appointment = Item.objects.get(id=id)
    except:
        return Response(
            {"res": "Object with appointment id does not exists"},
            status=status.HTTP_400_BAD_REQUEST,
        )
    serializer = ItemSerializer(instance=appointment, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["DELETE"])
def delete(id, *args, **kwargs):
    try:
        appointment = Item.objects.get(id=id)
    except:
        return Response(
            {"res": "Object with appointment id does not exists"},
            status=status.HTTP_400_BAD_REQUEST,
        )
    appointment.delete()
    return Response({"res": "Object deleted!"}, status=status.HTTP_200_OK)