from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Room
from .serializers import RoomSerializer


@api_view(["POST"])
def create(request):
    serializer = RoomSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def get_all(request):
    rooms = Room.objects.all()
    serializer = RoomSerializer(rooms, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def get_detail(request, id):
    try:
        item_instance = Room.objects.get(id=id)
    except:
        return Response(
            {"res": "Room with id does not exists"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    serializer = RoomSerializer(item_instance)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["PUT"])
def update(request, id):
    try:
        room = Room.objects.get(id=id)
    except:
        return Response(
            {"res": "Object with room id does not exists"},
            status=status.HTTP_400_BAD_REQUEST,
        )
    serializer = RoomSerializer(instance=room, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["PUT"])
def update_bed_number(request, id):
    try:
        room = Room.objects.get(id=id)
    except:
        return Response(
            {"res": "Object with room id does not exists"},
            status=status.HTTP_400_BAD_REQUEST,
        )
    room.bed_number = request.data.get("bed_number", room.bed_number)
    room.save()
    return Response({"res": "Update bed number successfull"}, status=status.HTTP_200_OK)

@api_view(["DELETE"])
def delete(id, *args, **kwargs):
    try:
        room = Room.objects.get(id=id)
    except:
        return Response(
            {"res": "Object with room id does not exists"},
            status=status.HTTP_400_BAD_REQUEST,
        )
    room.delete()
    return Response({"res": "Object deleted!"}, status=status.HTTP_200_OK)