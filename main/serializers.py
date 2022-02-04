from rest_framework import serializers
from .models import Alert, Drug, DrugBatch

class AlertSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Alert
        fields = '__all__'



class DrugSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Alert
        fields = '__all__'



class DrugBatchSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Alert
        fields = '__all__'
