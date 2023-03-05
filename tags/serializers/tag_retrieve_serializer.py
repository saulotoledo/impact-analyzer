from rest_framework import serializers
from django.core.validators import RegexValidator
from tags.models import Tag


class TagRetrieveSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()
    parent_id = serializers.SerializerMethodField()

    class Meta:
        model = Tag
        fields = ['id', 'name', 'children', 'parent_id']
        read_only_fields = ['id']

    def get_parent_id(self, obj):
        parent = obj.get_parent()
        if parent:
            return parent.id
        return None

    def get_children(self, obj):
        children = obj.get_children()
        serializer = self.__class__(children, many=True)
        return serializer.data
