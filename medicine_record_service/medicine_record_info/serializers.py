from rest_framework import serializers
from .models import Item, Dianosis, Treatment, Prescription

class PrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescription
        fields = '__all__'

class TreatmentSerializer(serializers.ModelSerializer):
    prescriptions = PrescriptionSerializer(many=True, write_only=True)

    class Meta:
        model = Treatment
        fields = ['id', 'name', 'desc', 'prescriptions']

    def create(self, validated_data):
        prescriptions_data = validated_data.pop('prescriptions')
        print(prescriptions_data)
        treatment = Treatment.objects.create(**validated_data)
        for prescription_data in prescriptions_data:
            Prescription.objects.create(treatment=treatment, **prescription_data)
        return treatment
    
    def update(self, instance, validated_data):
        prescriptions_data = validated_data.pop('prescriptions', None)
        if prescriptions_data is not None:
            # Xóa tất cả các prescription cũ
            instance.prescriptions.all().delete()
            for prescription_data in prescriptions_data:
                Prescription.objects.create(treatment=instance, **prescription_data)

        instance.name = validated_data.get('name', instance.name)
        instance.desc = validated_data.get('desc', instance.desc)
        instance.save()
        return instance

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        print(instance.prescriptions)
        print(PrescriptionSerializer(instance.prescriptions.all(), many=True).data)
        representation['prescriptions'] = PrescriptionSerializer(instance.prescriptions.all(), many=True).data
        return representation

class DianosisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dianosis
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    treatment = TreatmentSerializer()
    dianosis = DianosisSerializer()

    class Meta:
        model = Item
        fields = '__all__'

    def create(self, validated_data):
        treatment_data = validated_data.pop('treatment')
        dianosis_data = validated_data.pop('dianosis')

        treatment_serializer = TreatmentSerializer(data=treatment_data)
        if treatment_serializer.is_valid():
            treatment = treatment_serializer.save()
            dianosis_serializer = DianosisSerializer(data=dianosis_data)
            if dianosis_serializer.is_valid():
                dianosis = dianosis_serializer.save()
                item = Item.objects.create(treatment=treatment, dianosis=dianosis, **validated_data)
                return item
            raise serializers.ValidationError("Invalid Dianosis data")
        raise serializers.ValidationError("Invalid Treatment data")
    
    def update(self, instance, validated_data):
        treatment_data = validated_data.pop('treatment')
        dianosis_data = validated_data.pop('dianosis')

        instance.patient_id = validated_data.get('patient_id', instance.patient_id)
        instance.doctor_id = validated_data.get('doctor_id', instance.doctor_id)
        instance.department_id = validated_data.get('department_id', instance.department_id)
        instance.visit_date = validated_data.get('visit_date', instance.visit_date)
        instance.note = validated_data.get('note', instance.note)

        treatment_serializer = TreatmentSerializer(instance.treatment, data=treatment_data)
        if treatment_serializer.is_valid():
            treatment_serializer.save()

        dianosis_serializer = DianosisSerializer(instance.dianosis, data=dianosis_data)
        if dianosis_serializer.is_valid():
            dianosis_serializer.save()

        instance.save()
        return instance