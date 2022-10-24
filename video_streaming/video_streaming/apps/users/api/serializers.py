from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from rest_framework import serializers

from apps.users.models import User


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    pass


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("email", "name", "last_name")


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

        def create(self, validated_data):
            user = User(**validated_data)
            user.set_password(validated_data["password"])
            user.save()
            return user


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("email", "name", "last_name")

        def to_representation(self, instance):
            return {
                "email": instance["email"],
                "name": instance["name"],
                "last_name": instance["last_name"],
            }


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("email", "name", "last_name")


class PasswordSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=128, min_length=8, write_only=True)
    password_confirm = serializers.CharField(
        max_length=128, min_length=8, write_only=True
    )

    def validate(self, data):
        if data["password"] != data["password_confirm"]:
            raise serializers.ValidationError(
                {"password_confirm": "Ambas contraseñas deben ser iguales"}
            )
        return data
