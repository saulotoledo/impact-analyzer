from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from tags.serializers import TagRetrieveSerializer


class TagRetrieveUpdateDestroyAPIView(APIView):
    http_method_names = ['get', 'put', 'delete']
    service = None
    serializer_class = None

    @swagger_auto_schema(
        responses={
            200: 'Success',
            400: 'Bad Request'
        },
        operation_summary='Retrieves a tag',
        operation_description='Retrieves a tag by ID',
    )
    def get(self, request, id=None):
        """Returns a single tag"""

        if id is None:
            return Response("invalid id", status=status.HTTP_400_BAD_REQUEST)

        tag = self.service.get_tag(id)
        serializer = self.serializer_class(tag)
        return Response(serializer.data)

    @swagger_auto_schema(
        method='put',
        request_body=TagRetrieveSerializer,
        responses={
            200: 'Success',
            400: 'Bad Request'
        },
        operation_summary='Updates a tag',
        operation_description='Updates a tag by ID',
    )
    @action(detail=True, methods=['put']) # Required by @swagger_auto_schema to generate the request body
    def put(self, request, id):
        """Updates a single tag"""

        tag = self.service.get_tag(id)
        serializer = self.serializer_class(tag, data=request.data, partial=True)
        if serializer.is_valid():
            tag = self.service.update_tag(tag, serializer.validated_data)
            serializer = self.serializer_class(tag)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        responses={
            204: 'No Content',
            400: 'Bad Request'
        },
        operation_summary='Deletes a tag',
        operation_description='Deletes a tag by ID',
    )
    def delete(self, request, id):
        """Deletes a single tag"""

        tag = self.service.get_tag(id)
        self.service.delete_tag(tag)
        return Response(status=status.HTTP_204_NO_CONTENT)
