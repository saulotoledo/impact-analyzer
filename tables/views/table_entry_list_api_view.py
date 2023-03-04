from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from tables.models import Table, TableEntry
from drf_yasg.utils import swagger_auto_schema


class TableEntryListAPIView(ListAPIView):
    http_method_names = ['get']
    serializer_class = None

    def get_queryset(self):
        return TableEntry.objects.filter(table__id=self.kwargs.get('table_id')).order_by('line')

    @swagger_auto_schema(
        responses={
            200: 'Success',
            400: 'Bad Request',
            404: 'Not Found'
        },
        operation_summary='Retrieves all table entries',
        operation_description='Retrieves all table entries',
    )
    def get(self, request, *args, **kwargs):
        get_object_or_404(Table, id=kwargs.get('table_id'))
        entries = self.get_queryset()
        grouped_entries = self.serializer_class.group_by_line(entries)
        return Response(grouped_entries, status=status.HTTP_200_OK)
