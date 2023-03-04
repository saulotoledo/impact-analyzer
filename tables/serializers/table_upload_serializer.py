from rest_framework import serializers


class TableUploadSerializer(serializers.Serializer):
    file = serializers.FileField()
