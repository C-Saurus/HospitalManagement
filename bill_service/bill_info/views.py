from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Payment, Bill
from .serializers import PaymentSerializer, BillSerializer


@api_view(["POST"])
def create(request):
    serializer = BillSerializer(data=request.data)
    # try:
    # except:
    #     return Response(
    #         {"res": "Type with id does not exists"},
    #         status=status.HTTP_400_BAD_REQUEST,
    #     )
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["PUT"])
def update(request, id):
    try:
        bill = Bill.objects.get(id=id)
    except:
        return Response(
            {"res": "Object with bill id does not exists"},
            status=status.HTTP_400_BAD_REQUEST,
        )
    serializer = BillSerializer(instance=bill, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def get_all(request):
    items = Bill.objects.all()
    serializer = BillSerializer(items, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def get_detail(request, id):
    try:
        item_instance = Bill.objects.get(id=id)
    except:
        return Response(
            {"res": "Bill with id does not exists"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    serializer = BillSerializer(item_instance)
    return Response(serializer.data, status=status.HTTP_200_OK)