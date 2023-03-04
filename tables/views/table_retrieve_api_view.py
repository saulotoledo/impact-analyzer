from rest_framework.generics import RetrieveAPIView
from tables.models import Table
from drf_yasg.utils import swagger_auto_schema


class TableRetrieveAPIView(RetrieveAPIView):
    http_method_names = ['get']
    queryset = Table.objects.all()
    serializer_class = None

    @swagger_auto_schema(
        responses={
            200: 'Success',
            400: 'Bad Request'
        },
        operation_summary='Retrieves a table',
        operation_description='Retrieves a table by ID',
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)