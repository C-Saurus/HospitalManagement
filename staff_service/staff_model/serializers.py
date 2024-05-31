from rest_framework import serializers
from .models import Fullname, Item, Role, Address, Department


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
        representation["role"] = RoleSerializer(instance.role).data
        representation["address"] = AddressSerializer(instance.address).data
        representation["department"] = DepartmentSerializer(instance.department).data
        return representation
        
class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = "__all__"

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"