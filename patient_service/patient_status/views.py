from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from patient_info.models import Status
from patient_info.serializers import StatusSerializer


# Create your views here.
@api_view(["POST"])
# @permission_classes([IsAuthenticated])
def create(request):
    serializer = StatusSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["PUT"])
# @permission_classes([IsAuthenticated])
def update(request, id):
    try:
        status = Status.objects.get(id=id)
    except:
        return Response(
            {"res": "Status with book id does not exists"},
            status=status.HTTP_400_BAD_REQUEST,
        )
    serializer = StatusSerializer(instance=status, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def get_all(request):
    list_status = Status.objects.all()
    serializer = StatusSerializer(list_status, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
