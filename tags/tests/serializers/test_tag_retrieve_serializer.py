from django.test import TestCase
from tags.models import Tag
from tags.serializers import TagRetrieveSerializer


class TagRetrieveSerializerTestCase(TestCase):
    def setUp(self):
        self.root_tag = Tag.add_root(name='Root Tag Retrieve Serializer test')
        self.first_child = self.root_tag.add_child(name='First Child Tag Retrieve Serializer test')
        self.second_child = self.root_tag.add_child(name='Second Child Tag Retrieve Serializer test')
        self.first_grandchild = self.second_child.add_child(name='First Grandchild Tag Retrieve Serializer test')

    def tearDown(self):
        self.root_tag.delete()

    def test_serializer_output(self):
        serializer = TagRetrieveSerializer(self.root_tag)

        expected_output = {
            'id': self.root_tag.id,
            'name': self.root_tag.name,
            'children': [
                {
                    'id': self.first_child.id,
                    'name': self.first_child.name,
                    'children': []
                },
                {
                    'id': self.second_child.id,
                    'name': self.second_child.name,
                    'children': [
                        {
                            'id': self.first_grandchild.id,
                            'name': self.first_grandchild.name,
                            'children': []
                        }
                    ]
                }
            ]
        }
        self.assertEqual(serializer.data, expected_output)
