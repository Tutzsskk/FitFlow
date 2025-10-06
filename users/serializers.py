# users/serializers.py

from rest_framework import serializers
from .models import CustomUser

# Serializer para LER e ATUALIZAR dados do perfil
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'username', 'first_name', 'last_name', 'height', 'weight', 'gender', 'date_of_birth']

# Serializer para CRIAR um novo usuário (registro)
class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    password2 = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = CustomUser
        fields = [
            'email', 
            'username', 
            'password', 
            'password2',   
            'height', 
            'weight', 
            'gender', 
            'date_of_birth'
            ]

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')

        if password != password2:
            raise serializers.ValidationError({"password": "As senhas devem ser iguais."})
        
        return attrs
    
    def create(self, validated_data):
        validated_data.pop('password2')
        # Usa o método create_user para garantir que a senha seja salva com hash
        user = CustomUser.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password'],
            height=validated_data.get('height', ''),
            weight=validated_data.get('weight', ''),
            gender=validated_data.get('gender', ''),
            date_of_birth=validated_data.get('date_of_birth', ''),

        )
        return user