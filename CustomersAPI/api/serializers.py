from rest_framework import serializers
from api.models import Customer


# serializes and deserializes json data
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'name', 'age', 'active')