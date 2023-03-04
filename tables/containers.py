from dependency_injector import containers, providers

from . import serializers, services, views


class TablesContainer(containers.DeclarativeContainer):

    config = providers.Configuration()

    table_processor_service = providers.Factory(
        services.TableProcessorService,
        config.TABLE_PROCESSING_BATCH_SIZE,
    )

    table_upload_view = providers.Factory(
        views.TableUploadView.as_view,
        serializer_class=serializers.TableUploadSerializer,
        service=table_processor_service,
    )

    table_retrieve_view = providers.Factory(
        views.TableRetrieveAPIView.as_view,
        serializer_class=serializers.TableSerializer,
    )

    table_entry_list_api_view = providers.Factory(
        views.TableEntryListAPIView.as_view,
        serializer_class=serializers.TableEntrySerializer,
    )

    table_entry_retrieve_update_api_view = providers.Factory(
        views.TableEntryRetrieveUpdateAPIView.as_view,
        serializer_class=serializers.TableEntrySerializer,
    )
