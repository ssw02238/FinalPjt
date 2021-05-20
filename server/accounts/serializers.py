from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    # serializing은 하지만 응답에는 포함시키지 않아 비번이니까!
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User 
        fields = ('username', 'password',)