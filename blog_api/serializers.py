from rest_framework import serializers
from blog.models import Post
from django.contrib.auth.models import User


class PostSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        fields = (
            "id",
            "author",
            "title",
            "body",
            "created",
        )
        model = Post

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "is_superuser",
                  "username", "email",
                  "is_staff", "is_active",
                  "date_joined", "first_name",
                  "last_name")
