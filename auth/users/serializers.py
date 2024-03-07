from .models import CustomUser
from rest_framework import serializers


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email', 'password',"name","phone","address","city","state","zip","country","is_bussiness","is_superuser")
        extra_kwargs = {'password': {'write_only': True}}
