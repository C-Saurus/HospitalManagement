from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Address, Fullname, Item, Role, Department
from .serializers import ItemSerializer
from django.db import transaction


@api_view(["POST"])
@transaction.atomic
def create(request):
    try:
        
        first_name = request.data.get("first_name")
        mid_name = request.data.get("mid_name")
        last_name = request.data.get("last_name")
        
        no_house = request.data.get("no_house")
        city = request.data.get("city")
        district = request.data.get("district")
        
        age = request.data.get("age")
        dob = request.data.get("dob")
        hire_date = request.data.get("hire_date")
        cccd = request.data.get("cccd")
        phone = request.data.get("phone")
        gender = request.data.get("gender")
        level = request.data.get("level")

        with transaction.atomic(): 
            try:
                staff_role = Role.objects.get(id=request.data.get("role"))
            except:
                return Response(
                    {"res": "Role with id does not exists"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            try:
                staff_department = Department.objects.get(id=request.data.get("department"))
            except:
                return Response(
                    {"res": "Department with id does not exists"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            
            new_address = Address.objects.create(
                no_house=no_house, city=city, district=district 
            )
            
            new_fullname = Fullname.objects.create(
                first_name=first_name, mid_name=mid_name, last_name=last_name, 
            )
            

            Item.objects.create(
                cccd=cccd, age=age, phone=phone, address=new_address,
                fullname=new_fullname, dob=dob, gender=gender,
                hire_date=hire_date, level=level,
                department=staff_department, role=staff_role
            )
            return Response(
                {"message": "Staff created"}, status=status.HTTP_201_CREATED
            )
    except Exception as e:
        return Response({"error": str(e)}, status=500)

@api_view(["GET"])
def get_all(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def get_detail(request, id):
    try:
        item_instance = Item.objects.get(id=id)
    except:
        return Response(
            {"res": "Staff with id does not exists"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    serializer = ItemSerializer(item_instance)
    return Response(serializer.data, status=status.HTTP_200_OK)
