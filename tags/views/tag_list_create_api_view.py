from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class TagListCreateAPIView(APIView):
    allowed_methods = ['get', 'post']
    service = None
    serializer_class = None

    def get(self, request):
        """Returns all tags in the database"""

        tags = self.service.get_all_tags()
        serializer = self.serializer_class(tags, many=True)
        return Response(serializer.data)

    def post(self, request):
        """Creates a new tag"""

        serializer = self.serializer_class (data=request.data)
        if serializer.is_valid():
            tag = self.service.create_tag(serializer.validated_data)
            serializer = self.serializer_class(tag)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
