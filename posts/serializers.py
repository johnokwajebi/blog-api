from django.contrib.auth import get_user_model
# from django.db.models import fields
from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):

    class Meta:

        fields = ('id', 'author', 'title', 'body', 'created_at',)
        model = Post


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()  ## using get_user_model ensure we refer to the correct user model
        fields = ('id', 'username',)
