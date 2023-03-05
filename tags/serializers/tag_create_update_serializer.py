from rest_framework import serializers
from django.core.validators import RegexValidator
from tags.models import Tag


class TagCreateUpdateSerializer(serializers.ModelSerializer):
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
        fields = ['id', 'name', 'parent_id']
        read_only_fields = ['id']

    def create(self, validated_data):
        # TODO: Consider refactoring below for clarity. See comment for details.
        # Keeping "parent_id" below for simplicity in this example, but at this point
        # this is actualy an instance of Tag. The same happens in the update method
        # later in this class.
        parent = validated_data.pop('parent_id', None)
        parent_tag = None

        # TODO: Move code below to a more appropriate place
        if parent:
            try:
                parent_tag = Tag.objects.get(id=parent.id)
                return parent_tag.add_child(**validated_data)
            except Tag.DoesNotExist:
                raise serializers.ValidationError('Invalid parent tag')

        return Tag.add_root(validated_data)

    def update(self, instance, validated_data):
        parent = validated_data.pop('parent_id', None)
        if parent:
            instance.parent = parent
        return super().update(instance, validated_data)
