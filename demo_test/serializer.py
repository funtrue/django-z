from rest_framework import serializers
from demo_test.models import Demo_Model

class DMSerializer(serializers.ModelSerializer):
    class Meta:
        model = Demo_Model
        fields = "__all__"
        

