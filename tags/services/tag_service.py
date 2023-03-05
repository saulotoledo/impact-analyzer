from typing import List, Dict
from tags.models import Tag


class TagService:
    def get_all_tags(self) -> List[Tag]:
        return Tag.objects.filter(depth=1)

    def get_tag(self, id: int) -> Tag:
        return Tag.objects.get(pk=id)

    def create_tag(self, validated_data: Dict) -> Tag:
        parent_id = validated_data.pop('parent_id', None)
        if parent_id:
            parent = self.get_tag(parent_id)
            return Tag.add_root(**validated_data, parent=parent)
        else:
            return Tag.add_root(**validated_data)

    def update_tag(self, tag: Tag, validated_data: Dict) -> None:
        for key, value in validated_data.items():
            setattr(tag, key, value)
        tag.save()

    def delete_tag(self, tag: Tag) -> None:
        tag.delete()
