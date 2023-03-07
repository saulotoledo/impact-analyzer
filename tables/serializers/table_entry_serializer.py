from rest_framework import serializers
from tables.models import TableEntry
from tags.models import Tag


class TableEntrySerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    line = serializers.ReadOnlyField()
    column = serializers.ReadOnlyField()
    value = serializers.ReadOnlyField()
    tags = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Tag.objects.all(), required=False
    )


    class Meta:
        model = TableEntry
        fields = ['id', 'line', 'column', 'value', 'tags']

    def group_by_line(entries):
        result = []
        current_line = None
        current_group = None

        for entry in entries:
            if current_line != entry.line:
                current_line = entry.line
                current_group = []
                result.append(current_group)

            current_group.append({
                'id': entry.id,
                'line': entry.line,
                'column': entry.column,
                'value': entry.value,
                'tags': [tag.id for tag in entry.tags.all()],
            })

        return result