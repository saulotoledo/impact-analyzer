from django.test import TestCase
from tags.models import Tag
from tags.serializers import TagCreateUpdateSerializer


class TagCreateUpdateSerializerTestCase(TestCase):
    def setUp(self):
        self.root_tag = Tag.add_root(name='Root Tag Retrieve Serializer test')
        self.first_child = self.root_tag.add_child(name='First Child Tag Retrieve Serializer test')
        self.second_child = self.root_tag.add_child(name='Second Child Tag Retrieve Serializer test')
        self.first_grandchild = self.second_child.add_child(name='First Grandchild Tag Retrieve Serializer test')

    def tearDown(self):
        self.first_grandchild.delete()
        self.first_child.delete()
        self.second_child.delete()
        self.root_tag.delete()

    def test_create_serializer_valid(self):
        data = {
            'name': 'New Tag',
            'parent_id': self.root_tag.id
        }
        serializer = TagCreateUpdateSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        tag = serializer.save()
        self.assertEqual(tag.name, data['name'])
        self.assertEqual(tag.path.__len__(), 8)
        self.assertTrue(tag.path.startswith(self.root_tag.path))

    def test_create_serializer_invalid(self):
        # The required field 'name' is missing
        data = {
            'parent_id': self.root_tag.id
        }
        serializer = TagCreateUpdateSerializer(data=data)
        self.assertFalse(serializer.is_valid())

    def test_update_serializer_valid(self):
        root_tag = Tag.add_root(name='Root Tag Update Serializer test')
        first_child = root_tag.add_child(name='First Child Tag Update Serializer test')
        data = {
            'name': 'Updated Tag',
            'parent_id': root_tag.id
        }
        serializer = TagCreateUpdateSerializer(first_child, data=data, partial=True)
        self.assertTrue(serializer.is_valid())
        tag = serializer.save()
        self.assertEqual(tag.name, data['name'])
        self.assertEqual(tag.parent.id, data['parent_id'])

    def test_update_serializer_invalid(self):
        root_tag = Tag.add_root(name='Root Tag Update Serializer test')
        first_child = root_tag.add_child(name='First Child Tag Update Serializer test')
        # The field 'parent_id' is invalid
        data = {
            'parent_id': 999
        }
        serializer = TagCreateUpdateSerializer(first_child, data=data, partial=True)
        self.assertFalse(serializer.is_valid())
