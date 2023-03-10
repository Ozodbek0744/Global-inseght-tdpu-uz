from .models import BlogVideo
from rest_framework import serializers
from accounts.models import Account


class BlogVideoListSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()

    class Meta:
        model = BlogVideo
        fields = [
            'id',
            'title',
            'description',
            'url',
            'author',
            'image',
            'slug',

        ]

    def get_author(self, obj):
        return f"{obj.author.famly} {obj.author.username} {obj.author.otchestvo}"

    def get_image(self, obj):
        return f"{obj.author.image}"


class BlogVideoSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()
    class Meta:
        model = BlogVideo
        fields = "__all__"

    def get_author(self, obj):
        return f"{obj.author.famly} {obj.author.username} {obj.author.otchestvo}"

    def get_image(self, obj):
        return f"{obj.author.image}"


class BlogVideoDetailSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()

    class Meta:
        model = BlogVideo
        fields = "__all__"

    def get_author(self, obj):
        return f"{obj.author.famly} {obj.author.username} {obj.author.otchestvo}"

    def get_image(self, obj):
        return f"{obj.author.image}"


class BlogVideoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogVideo
        fields = ['title', 'description', 'url']


