from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from tags.serializers import TagCreateUpdateSerializer


class TagListCreateAPIView(APIView):
    http_method_names = ['get', 'post']
    service = None
    retrieve_serializer_class = None
    create_update_serializer_class = None

    @swagger_auto_schema(
        responses={
            200: 'Success',
            400: 'Bad Request'
        },
        operation_summary='Retrieves all tags',
        operation_description='Retrieves all tags',
    )
    def get(self, request):
        """Returns all tags in the database"""

        tags = self.service.get_all_tags()
        serializer = self.retrieve_serializer_class(tags, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        method='post',
        request_body=TagCreateUpdateSerializer,
        responses={
            201: 'Created',
            400: 'Bad Request'
        },
        operation_summary='Creates a tag',
        operation_description='Creates a new tag',
    )
    @action(detail=True, methods=['post']) # Required by @swagger_auto_schema to generate the request body
    def post(self, request):
        """Creates a new tag"""

        serializer = self.create_update_serializer_class(data=request.data)
        if serializer.is_valid():
            tag = self.service.create_tag(serializer.validated_data)
            serializer = self.retrieve_serializer_class(tag)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
