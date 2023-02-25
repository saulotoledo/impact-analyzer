from rest_framework import serializers
from django.core.validators import RegexValidator
from tags.models import Tag


class TagSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        max_length=120,
        validators=[
            RegexValidator(
                regex=r'^[a-zA-Z0-9][a-zA-Z0-9\s]*$',
                message='Name must start with a letter or number and contain only letters, numbers, or spaces.'
            )
        ]
    )
    parent_id = serializers.PrimaryKeyRelatedField(
        queryset=Tag.objects.all(),
        required=False,
        allow_null=True,
    )

    class Meta:
        model = Tag
        fields = ['id', 'path', 'depth', 'numchild', 'name', 'parent_id']
        read_only_fields = ['id', 'path', 'depth', 'numchild']

    def update(self, instance, validated_data):
        parent_id = validated_data.pop('parent_id', None)
        if parent_id:
            instance.parent = parent_id
        return super().update(instance, validated_data)
