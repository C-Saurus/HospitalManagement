from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from staff_model.models import Address, Fullname, Item, Role, Department
from staff_model.serializers import ItemSerializer
from django.db import transaction


@api_view(["PUT"])
@transaction.atomic
def update(request, id):
    try:
        with transaction.atomic():                        
            try:
                staff = Item.objects.get(id=id)
            except:
                return Response(
                    {"res": "Staff with id does not exists"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            
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
                    {"res": "Type with id does not exists"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
                
            age = request.data.get("age", staff.age)
            dob = request.data.get("dob", staff.dob)
            hire_date = request.data.get("hire_date", staff.hire_date)
            cccd = request.data.get("cccd", staff.cccd)
            phone = request.data.get("phone", staff.phone)
            gender = request.data.get("gender", staff.gender)
            level = request.data.get("level", staff.level)
            
            new_address = Address.objects.get(id=staff.address.id)
            new_address.no_house = request.data.get("no_house", new_address.no_house)
            new_address.city = request.data.get("city", new_address.city)
            new_address.district = request.data.get("district", new_address.district)
            new_address.save()
            
            new_fullname = Fullname.objects.get(id=staff.fullname.id)
            new_fullname.first_name = request.data.get("first_name", new_fullname.first_name)
            new_fullname.mid_name = request.data.get("mid_name", new_fullname.mid_name)
            new_fullname.last_name = request.data.get("last_name", new_fullname.last_name)
            new_fullname.save()
            
            staff.cccd = cccd
            staff.age = age
            staff.phone = phone
            staff.dob = dob
            staff.hire_date = hire_date
            staff.gender = gender
            staff.department = staff_department
            staff.role = staff_role
            staff.level = level
            staff.save()
            return Response(
                {"message": "Staff updated"}, status=status.HTTP_200_OK
            )
    except Exception as e:
        return Response({"error": str(e)}, status=500)
    
@api_view(["PUT"])
def update_department(request, id):
    try:
        staff = Item.objects.get(id=id)
    except:
        return Response(
            {"res": "Staff with id does not exists"},
            status=status.HTTP_400_BAD_REQUEST,
        )
            
    try:
        staff_department = Department.objects.get(id=request.data.get("department"))
    except:
        return Response(
            {"res": "Status with id does not exists"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    staff.department = staff_department
    staff.save()
    return Response(
        {"message": "Staff department updated"}, status=status.HTTP_200_OK
    )

@api_view(["PUT"])
def update_level(request, id):
    try:
        staff = Item.objects.get(id=id)
    except:
        return Response(
            {"res": "Staff with id does not exists"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    staff.level = request.data.get("level", staff.level)
    staff.save()
    return Response(
        {"message": "Staff level updated"}, status=status.HTTP_200_OK
    )

@api_view(["DELETE"])
@transaction.atomic
def delete(id, *args, **kwargs):
    try:
        with transaction.atomic(): 
            try:
                staff = Item.objects.get(id=id)
            except:
                return Response(
                    {"res": "Object with staff id does not exists"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            
            address = Address.objects.get(id=staff.address.id)
            address.delete()
            
            fullname = Fullname.objects.get(id=staff.fullname.id)
            fullname.delete()
            
            staff.delete()
            return Response({"res": "Object deleted!"}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=500)