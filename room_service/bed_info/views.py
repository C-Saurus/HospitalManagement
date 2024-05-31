from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from room_info.models import Bed, Room
from room_info.serializers import BedSerializer, RoomSerializer


@api_view(["POST"])
def create(request):
    serializer = BedSerializer(data=request.data)
    try:
        Room.objects.get(id=request.data.get("room"))
    except:
        return Response(
            {"res": "Room with id does not exists"},
            status=status.HTTP_400_BAD_REQUEST,
        )
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def get_all(request):
    rooms = Bed.objects.all()
    serializer = BedSerializer(rooms, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def get_detail(request, id):
    try:
        item_instance = Bed.objects.get(id=id)
    except:
        return Response(
            {"res": "Bed with id does not exists"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    serializer = BedSerializer(item_instance)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["PUT"])
def update(request, id):
    try:
        bed = Bed.objects.get(id=id)
    except:
        return Response(
            {"res": "Object with bed id does not exists"},
            status=status.HTTP_400_BAD_REQUEST,
        )
    
    serializer = BedSerializer(instance=bed, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["PUT"])
def update_status(request, id):
    try:
        bed = Bed.objects.get(id=id)
    except:
        return Response(
            {"res": "Object with bed id does not exists"},
            status=status.HTTP_404_NOT_FOUND,
        )
    if (bed.status == request.data.get("status", bed.status) and bed.status == "Busy"):
        return Response(
            {"res": "Object with bed is busy"},
            status=status.HTTP_400_BAD_REQUEST,
        )
    bed.status = request.data.get("status", bed.status)
    bed.save()
    return Response({"res": "Update bed status successfull"}, status=status.HTTP_200_OK)

@api_view(["DELETE"])
def delete(id, *args, **kwargs):
    try:
        bed = Bed.objects.get(id=id)
    except:
        return Response(
            {"res": "Object with bed id does not exists"},
            status=status.HTTP_400_BAD_REQUEST,
        )
    bed.delete()
    return Response({"res": "Object deleted!"}, status=status.HTTP_200_OK)