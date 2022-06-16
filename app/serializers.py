from ast import Not
from dataclasses import field
from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id','username','email','first_name','last_name','password']
        extra_kwargs = {
            'pas sword': {'write_only': True},
            'username': {'label':'hello'}
        }
        
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data) # **validated data is the validated data without the extracted password
        if password is not None:
            instance.set_password(password) # set_password method hashes the password
            instance.save()
            return instance
       
