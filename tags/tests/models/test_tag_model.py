from django.test import TestCase
from tags.models import Tag


class TagModelTestCase(TestCase):
    def setUp(self):
        self.rootTag = Tag.add_root(name='Root Tag Model test')
        childNode1 = self.rootTag.add_child(name='Second level tag 1')
        childNode2 = childNode1.add_sibling(name='Second level tag 2')
        childNode2.add_child(name='Third level tag')

    def tearDown(self):
        self.rootTag.delete()

    def test_root_tag_name(self):
        tag_name = self.rootTag.name
        self.assertEqual(tag_name, 'Root Tag Model test')

    def test_root_tag_str(self):
        tag_str = str(self.rootTag)
        self.assertEqual(tag_str, 'Root Tag Model test')

    def test_tags_num_children(self):
        # When using .add_siblings(), .numchild is not incremented. So, we use .count() below
        # TODO: Review test and link official documentation explaining the behavior above
        self.assertEqual(self.rootTag.get_children().count(), 2)
        self.assertEqual(self.rootTag.get_children()[1].numchild, 1)

    def test_children_tag_names(self):
        root_children = self.rootTag.get_children()
        self.assertEqual(root_children[0].name, 'Second level tag 1')
        self.assertEqual(root_children[1].name, 'Second level tag 2')
        self.assertEqual(root_children[1].get_children()[0].name, 'Third level tag')
