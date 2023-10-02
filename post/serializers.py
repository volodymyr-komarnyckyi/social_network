from rest_framework import serializers
from .models import Post
from user.serializers import UserEmailSerializer


class PostSerializer(serializers.ModelSerializer):
    user = UserEmailSerializer()
    likes = UserEmailSerializer(many=True, read_only=True)
    likes_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ('id', 'user', 'content', 'created_at', "likes_count", 'likes')
        read_only_fields = ('id', 'user', 'created_at', "likes_count", 'likes')

    def get_likes_count(self, obj):
        return obj.likes.count()


class LikeActionSerializer(serializers.Serializer):
    pass
