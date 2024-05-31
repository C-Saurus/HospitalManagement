from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from patient_info.models import RentInfo, Item
from patient_info.serializers import RentInfoSerializer
import requests

# Create your views here.
@api_view(["POST"])
# @permission_classes([IsAuthenticated])
def create(request):
    serializer = RentInfoSerializer(data=request.data)
    try:
        Item.objects.get(id=request.data.get("patient_id"))
    except:
        return Response(
            {"res": "Patient with id does not exists"},
            status=status.HTTP_400_BAD_REQUEST,
        )
    try:
        bed_id = request.data.get("bed_id")
        data = {
            "status": "Busy"
        }
        res = requests.put(f"http://127.0.0.1:8003/bed/{bed_id}/update_status", data=data)
        if (res.status_code != 200):
            if (res.status_code == 400):
                return Response(
                {"res": "Bed with id is busy"},
                status=status.HTTP_400_BAD_REQUEST,
                )
            else:
                return Response(
                {"res": "Bed with id is not exist"},
                status=status.HTTP_400_BAD_REQUEST,
                )
    except:
        return Response(
            {"res": "Bed with id is busy"},
            status=status.HTTP_400_BAD_REQUEST,
        )
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["PUT"])
# @permission_classes([IsAuthenticated])
def update(request, id):
    try:
        rent_info = RentInfo.objects.get(id=id)
    except:
        return Response(
            {"res": "RentInfo with book id does not exists"},
            status=status.HTTP_400_BAD_REQUEST,
        )
    serializer = RentInfoSerializer(instance=rent_info, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def get_all(request):
    list_rent = RentInfo.objects.all()
    serializer = RentInfoSerializer(list_rent, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["GET"])
def get_by_patient_id(request, id):
    list_rent = RentInfo.objects.filter(patient_id=id)
    serializer = RentInfoSerializer(list_rent, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)