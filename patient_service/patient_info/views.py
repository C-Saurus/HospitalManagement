from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Relatives, Address, Fullname, Item, Status, Type
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
        
        relatives_name = request.data.get("relatives_name")
        relatives_phone = request.data.get("relatives_phone")
        
        age = request.data.get("age")
        dob = request.data.get("dob")
        cccd = request.data.get("cccd")
        phone = request.data.get("phone")
        gender = request.data.get("gender")

        with transaction.atomic(): 
            try:
                patient_status = Status.objects.get(id=request.data.get("status"))
            except:
                return Response(
                    {"res": "Status with id does not exists"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            try:
                patient_type = Type.objects.get(id=request.data.get("type"))
            except:
                return Response(
                    {"res": "Type with id does not exists"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
               
            new_relatives = Relatives.objects.create(
                name=relatives_name, phone=relatives_phone, 
            )
            
            new_address = Address.objects.create(
                no_house=no_house, city=city, district=district 
            )
            
            new_fullname = Fullname.objects.create(
                first_name=first_name, mid_name=mid_name, last_name=last_name, 
            )
            

            Item.objects.create(
                cccd=cccd, age=age, phone=phone, 
                relatives=new_relatives, address=new_address,
                fullname=new_fullname, dob=dob, gender=gender,
                type=patient_type, status=patient_status
            )
            return Response(
                {"message": "Patient created"}, status=status.HTTP_201_CREATED
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
            {"res": "Patient with id does not exists"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    serializer = ItemSerializer(item_instance)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["PUT"])
@transaction.atomic
def update(request, id):
    try:
        with transaction.atomic():                        
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

            try:
                patient_type = Type.objects.get(id=request.data.get("type"))
            except:
                return Response(
                    {"res": "Type with id does not exists"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
                
            age = request.data.get("age", patient.age)
            dob = request.data.get("dob", patient.dob)
            cccd = request.data.get("cccd", patient.cccd)
            phone = request.data.get("phone", patient.phone)
            gender = request.data.get("gender", patient.gender)
            
            new_relatives = Relatives.objects.get(id=patient.relatives.id)
            new_relatives.name = request.data.get("relatives_name", new_relatives.name)
            new_relatives.phone = request.data.get("relatives_phone", new_relatives.phone)
            new_relatives.save()
            
            new_address = Address.objects.get(id=patient.address.id)
            new_address.no_house = request.data.get("no_house", new_address.no_house)
            new_address.city = request.data.get("city", new_address.city)
            new_address.district = request.data.get("district", new_address.district)
            new_address.save()
            
            new_fullname = Fullname.objects.get(id=patient.fullname.id)
            new_fullname.first_name = request.data.get("first_name", new_fullname.first_name)
            new_fullname.mid_name = request.data.get("mid_name", new_fullname.mid_name)
            new_fullname.last_name = request.data.get("last_name", new_fullname.last_name)
            new_fullname.save()
            
            patient.cccd = cccd
            patient.age = age
            patient.phone = phone
            patient.dob = dob
            patient.gender = gender
            patient.type = patient_type
            patient.save()
            return Response(
                {"message": "Patient updated"}, status=status.HTTP_200_OK
            )
    except Exception as e:
        return Response({"error": str(e)}, status=500)

@api_view(["DELETE"])
@transaction.atomic
def delete(id, *args, **kwargs):
    try:
        with transaction.atomic(): 
            try:
                patient = Item.objects.get(id=id)
            except:
                return Response(
                    {"res": "Object with patient id does not exists"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            relatives = Relatives.objects.get(id=patient.relatives.id)
            relatives.delete()
            
            address = Address.objects.get(id=patient.address.id)
            address.delete()
            
            fullname = Fullname.objects.get(id=patient.fullname.id)
            fullname.delete()
            
            patient.delete()
            return Response({"res": "Object deleted!"}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=500)
