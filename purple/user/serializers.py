from dataclasses import field
from rest_framework.serializers import ModelSerializer,Serializer
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from user.models import Account

class UserSerializer(ModelSerializer):
    class Meta:
        model = Account
        fields =  '__all__' 
    

class AccountSerializer(ModelSerializer):
    account = UserSerializer()
    class Meta:
        model = Account
    
    def update(self, instance, validated_data):
        account = validated_data.pop('account')
        account_serializer = AccountSerializer(instance.account, data=account)
        account_serializer.is_valid(raise_exception=True)
        account_serializer.save()
        return super(UserSerializer, self).update(instance, validated_data)


class ChangePasswordSerializer(Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate_new_password(self, value):
        validate_password(value)
        return value

class RegisterSerializer(ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = Account
        fields =  '__all__' 

        def validate(self, attr):
            validate_password(attr['password'])
            return attr
        
        def create(self, validated_data):
            user = Account.objects.create(
                username = validated_data['username']
            )
            user.set_password(validated_data['password'])
            user.save()