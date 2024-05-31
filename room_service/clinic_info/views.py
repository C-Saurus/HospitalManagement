from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from room_info.models import Clinic
from room_info.serializers import ClinicSerializer


@api_view(["POST"])
def create(request):
    serializer = ClinicSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def get_all(request):
    rooms = Clinic.objects.all()
    serializer = ClinicSerializer(rooms, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def get_detail(request, id):
    try:
        item_instance = Clinic.objects.get(id=id)
    except:
        return Response(
            {"res": "Clinic with id does not exists"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    serializer = ClinicSerializer(item_instance)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["PUT"])
def update(request, id):
    try:
        clinic = Clinic.objects.get(id=id)
    except:
        return Response(
            {"res": "Object with clinic id does not exists"},
            status=status.HTTP_400_BAD_REQUEST,
        )
    
    serializer = ClinicSerializer(instance=clinic, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["PUT"])
def update_status(request, id):
    try:
        clinic = Clinic.objects.get(id=id)
    except:
        return Response(
            {"res": "Object with clinic id does not exists"},
            status=status.HTTP_400_BAD_REQUEST,
        )
    clinic.status = request.data.get("status", clinic.status)
    clinic.save()
    return Response({"res": "Update clinic status successfull"}, status=status.HTTP_200_OK)

@api_view(["DELETE"])
def delete(id, *args, **kwargs):
    try:
        clinic = Clinic.objects.get(id=id)
    except:
        return Response(
            {"res": "Object with clinic id does not exists"},
            status=status.HTTP_400_BAD_REQUEST,
        )
    clinic.delete()
    return Response({"res": "Object deleted!"}, status=status.HTTP_200_OK)