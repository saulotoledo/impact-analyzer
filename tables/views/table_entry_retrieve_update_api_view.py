from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action
from rest_framework.generics import RetrieveUpdateAPIView
from tables.models import TableEntry
from tables.models import Table
from tables.serializers import TableEntrySerializer


class TableEntryRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    http_method_names = ['get', 'put']
    serializer_class = None

    def get_queryset(self):
        return TableEntry.objects.filter(table__id=self.kwargs.get('table_id'))

    def perform_update(self, serializer):
        table_id = self.kwargs.get('table_id')
        table = get_object_or_404(Table, id=table_id)
        serializer.save(table=table)

    @swagger_auto_schema(
        responses={
            200: 'Success',
            400: 'Bad Request'
        },
        operation_summary='Retrieves a table entry',
        operation_description='Retrieves a table entry by ID',
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        method='put',
        request_body=TableEntrySerializer,
        responses={
            200: 'Success',
            400: 'Bad Request'
        },
        operation_summary='Updates a table entry',
        operation_description='Update a table entry by ID. Only the tags can be updated. All other fields are read-only.',
    )
    @action(detail=True, methods=['put']) # Required by @swagger_auto_schema to generate the request body
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)
