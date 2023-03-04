from django.urls import path
from impact_analyzer.containers import get_container


container = get_container().tables_package.container

urlpatterns = [
    path('upload', container.table_upload_view(), name='table-list'),
    path('<int:pk>', container.table_retrieve_view(), name='table-detail'),
    path('<int:table_id>/entry/', container.table_entry_list_api_view(), name='entry-list'),
    path('<int:table_id>/entry/<int:pk>/', container.table_entry_retrieve_update_api_view(), name='entry-detail-update'),
]
