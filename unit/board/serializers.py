from rest_framework import serializers
from .models import Board, Comment

class BoardSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Board
        fields = (
            'url',
            'pk',
            'title',
            'views',
            'content',
            'writer',
            'tag',
            'created',
            'updated',
        )

class CommentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Comment
        fields = (
            'url',
            'board',
            'content',
            'writer',
            'created',
            'updated',
        )