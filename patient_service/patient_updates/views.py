from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from patient_info.models import Item, Status

@api_view(["PUT"])
def update_status(request, id):
    try:
        patient = Item.objects.get(id=id)
    except:
        return Response(
            {"res": "Patient with id does not exists"},
            status=status.HTTP_400_BAD_REQUEST,
        )
            
    try:
        patient_status = Status.objects.get(id=request.data.get("status"))
    except:
        return Response(
            {"res": "Status with id does not exists"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    patient.status = patient_status
    patient.save()
    return Response(
        {"message": "Patient status updated"}, status=status.HTTP_200_OK
    )