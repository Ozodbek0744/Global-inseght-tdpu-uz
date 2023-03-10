from rest_framework import serializers
from .models import News


class NewsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = [
            'title',
            'description',
            'image',
            'date_created',
            'slug'
        ]


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = [
            'id',
            'title',
            'description',
            'image',
            'author',
            'date_created',
            'slug'

        ]


class NewsUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = [
            'title',
            'description',
            'image'
        ]

