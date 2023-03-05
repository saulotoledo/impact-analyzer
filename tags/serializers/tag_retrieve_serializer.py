from rest_framework import serializers
from django.core.validators import RegexValidator
from tags.models import Tag


class TagRetrieveSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    class Meta:
        model = Tag
        fields = ['id', 'name', 'children']
        read_only_fields = ['id']

    def get_children(self, obj):
        children = obj.get_children()
        serializer = self.__class__(children, many=True)
        return serializer.data
