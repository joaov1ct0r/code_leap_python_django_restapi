from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["id", "username", "created_datetime", "title", "content"]

class PostSchemaPostSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=50)
    title = serializers.CharField(max_length=70)
    content = serializers.CharField(max_length=100)

class PostSchemaPatchSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=70)
    content = serializers.CharField(max_length=100)