from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from bill_info.models import Bill, Payment
from bill_info.serializers import PaymentSerializer


@api_view(["POST"])
def create(request):
    serializer = PaymentSerializer(data=request.data)
    try:
        Bill.objects.get(id=request.data.get("bill"))
    except:
        return Response(
            {"res": "Bill with id does not exists"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["PUT"])
def update(request, id):
    try:
        payment = Payment.objects.get(id=id)
    except:
        return Response(
            {"res": "Object with payment id does not exists"},
            status=status.HTTP_400_BAD_REQUEST,
        )
    try:
        bill = Bill.objects.get(id=payment.bill.id)
    except:
        return Response(
            {"res": "Object with bill id does not exists"},
            status=status.HTTP_400_BAD_REQUEST,
        )
    bill.status = request.data.get("type")
    bill.save()
    serializer = PaymentSerializer(instance=payment, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def get_all():
    items = Payment.objects.all()
    serializer = PaymentSerializer(items, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def get_detail(request, id):
    try:
        item_instance = Payment.objects.get(id=id)
    except:
        return Response(
            {"res": "Payment with id does not exists"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    serializer = PaymentSerializer(item_instance)
    return Response(serializer.data, status=status.HTTP_200_OK)