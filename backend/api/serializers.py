from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Note

#Code your ORM here to convert json data to python code and vice versa
#kwargs in Python is a special syntax that allows you to pass a keyworded, variable-length argument dictionary to a function. It is short for "keyword arguments".


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["id", "title", "content", "created_at", "author"]
        extra_kwargs = {"author": {"read-only": True}}
