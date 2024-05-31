from rest_framework import serializers
from .models import Fullname, Item, Type, Address, Status, Relatives, RentInfo


class FullnameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fullname
        fields = "__all__"


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["fullname"] = FullnameSerializer(instance.fullname).data
        representation["type"] = TypeSerializer(instance.type).data
        representation["address"] = AddressSerializer(instance.address).data
        representation["status"] = StatusSerializer(instance.status).data
        representation["relatives"] = RelativesSerializer(instance.relatives).data
        return representation
        
class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = "__all__"

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = "__all__"
        
class RelativesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Relatives
        fields = "__all__"
        
class RentInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentInfo
        fields = "__all__"