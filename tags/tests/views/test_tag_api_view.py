from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from tags.models import Tag
from tags.serializers import TagRetrieveSerializer


class TagListCreateAPIViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.tags = [
            Tag.add_root(name='Tag 1'),
            Tag.add_root(name='Tag 2'),
            Tag.add_root(name='Tag 3'),
        ]

    def tearDown(self):
        for tag in self.tags:
            tag.delete()

    def test_create_tag(self):
        url = reverse('tag-list-create')
        data = {'name': 'New Tag'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_all_tags(self):
        url = reverse('tag-list-create')
        response = self.client.get(url)
        serializedTags = TagRetrieveSerializer(self.tags, many=True).data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializedTags)

    def test_retrieve_single_tag(self):
        tagToCheck = self.tags[1]
        url = reverse('tag-retrieve-update-destroy', kwargs={"id": tagToCheck.id})
        response = self.client.get(url)
        serializedTag = TagRetrieveSerializer(instance=tagToCheck).data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializedTag)

    def test_update_tag(self):
        tagToUpdate = self.tags[2]
        url = reverse('tag-retrieve-update-destroy', kwargs={"id": tagToUpdate.id})
        data = {'name': 'Updated Test Tag'}
        response = self.client.put(url, data=data)

        tagToUpdate.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(tagToUpdate.name, data['name'])

    def test_delete_tag(self):
        tagToUpdate = self.tags[2]
        url = reverse('tag-retrieve-update-destroy', kwargs={"id": tagToUpdate.id})
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Tag.objects.filter(id=tagToUpdate.id).exists())
