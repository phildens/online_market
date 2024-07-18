from rest_framework import serializers
from django.contrib.auth.models import User
from user_buyer.models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        print(validated_data)
        user = CustomUser(
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            address=validated_data["address"],
            city=validated_data["city"],
            phone=validated_data["phone"],
            username=validated_data["username"],
        )
        user.set_password(validated_data["password"])
        user.save()
        return user