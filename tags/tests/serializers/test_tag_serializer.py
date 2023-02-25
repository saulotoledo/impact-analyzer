from django.test import TestCase
from tags.models import Tag
from tags.serializers import TagSerializer


class TagSerializerTestCase(TestCase):
    def setUp(self):
        self.tag = Tag.add_root(name='Root Tag Serializer test')

    def tearDown(self):
        self.tag.delete()

    def test_serializer_output(self):
        serializer = TagSerializer(self.tag)

        expected_output = {
            'id': self.tag.id,
            'path': self.tag.path,
            'depth': self.tag.depth,
            'numchild': self.tag.numchild,
            'name': self.tag.name
        }
        self.assertEqual(serializer.data, expected_output)
