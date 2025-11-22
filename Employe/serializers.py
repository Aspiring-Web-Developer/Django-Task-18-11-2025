from rest_framework import serializers
from .models import *

class Department_serializers(serializers.ModelSerializer):
    class Meta:
        model = Department_Model
        fields="__all__"
        fields =['id', 'name', 'employee']

class Employe_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Employe_Model
        fields = "__all__"

class Profile_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Profile_Model
        fields = "__all__"