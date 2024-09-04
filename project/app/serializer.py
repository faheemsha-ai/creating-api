from . models import Address
from rest_framework import serializers

class AddressSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields= ["id","name","Address","phone"]