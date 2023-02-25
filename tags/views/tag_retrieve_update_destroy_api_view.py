from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class TagRetrieveUpdateDestroyAPIView(APIView):
    allowed_methods = ['get', 'put', 'delete']
    service = None
    serializer_class = None

    def get(self, request, id=None):
        """Returns a single tag"""

        if id is None:
            return Response("invalid id", status=status.HTTP_400_BAD_REQUEST)

        tag = self.service.get_tag(id)
        serializer = self.serializer_class(tag)
        return Response(serializer.data)

    def put(self, request, id):
        """Updates a single tag"""

        tag = self.service.get_tag(id)
        serializer = self.serializer_class(tag, data=request.data, partial=True)
        if serializer.is_valid():
            tag = self.service.update_tag(tag, serializer.validated_data)
            serializer = self.serializer_class(tag)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        """Deletes a single tag"""

        tag = self.service.get_tag(id)
        self.service.delete_tag(tag)
        return Response(status=status.HTTP_204_NO_CONTENT)
