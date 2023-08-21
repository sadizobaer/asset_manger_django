from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Asset, AssignManager
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password


class AssetSrializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = "__all__"


class AssignManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssignManager
        fields = "__all__"

    def get_asset_id(self, obj):
        return obj.asset.asset_id

    def get_username_assigned_to(self, obj):
        return obj.assigned_to.username

    def get_username_assigned_by(self, obj):
        return obj.assigned_by.username

    def to_representation(self, obj):
        representation = super().to_representation(obj)
        representation["asset_id"] = self.get_asset_id(obj)
        representation["assigned_to_name"] = self.get_username_assigned_to(obj)
        representation["assigned_by_name"] = self.get_username_assigned_by(obj)
        return representation


class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(required=True, validators=[validate_password], write_only=True)

    class Meta:
        model = User
        fields = ("username", "password", "email")

    def create(self, validated_data):
        user = User.objects.create(username=validated_data["username"], email=validated_data["email"])
        user.set_password(raw_password=validated_data["password"])
        user.save()
        return user
