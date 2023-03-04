from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class TableUploadView(APIView):
    parser_classes = [MultiPartParser]
    serializer_class = None
    service = None

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name="file",
                in_=openapi.IN_FORM,
                type=openapi.TYPE_FILE,
                required=True,
                description="Table"
            )
        ],
        operation_summary='Creates a new table by uploading a CSV file',
        operation_description='Creates a new table by uploading a CSV file',
    )
    @action(detail=False, methods=['post'], parser_classes=(MultiPartParser), name='upload-table', url_path='upload-table')
    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            file = request.FILES['file']
            self.service.parse_csv_table(file.name, file)

            return Response({'message': 'File uploaded successfully.'}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
