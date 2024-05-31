from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from appointment_info.models import Type
from appointment_info.serializers import TypeSerializer


# Create your views here.
@api_view(["POST"])
# @permission_classes([IsAuthenticated])
def create(request):
    serializer = TypeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["PUT"])
# @permission_classes([IsAuthenticated])
def update(request, id):
    try:
        status = Type.objects.get(id=id)
    except:
        return Response(
            {"res": "Type with id does not exists"},
            status=status.HTTP_400_BAD_REQUEST,
        )
    serializer = TypeSerializer(instance=status, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def get_all(request):
    list_status = Type.objects.all()
    serializer = TypeSerializer(list_status, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
