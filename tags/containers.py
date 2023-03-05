from dependency_injector import containers, providers

from . import serializers, services, views


class TagsContainer(containers.DeclarativeContainer):

    config = providers.Configuration()

    tag_service = providers.Factory(services.TagService)

    tag_list_create_api_view = providers.Factory(
        views.TagListCreateAPIView.as_view,
        create_update_serializer_class=serializers.TagCreateUpdateSerializer,
        retrieve_serializer_class=serializers.TagRetrieveSerializer,
        service=tag_service,
    )

    tag_retrieve_update_destroy_api_view = providers.Factory(
        views.TagRetrieveUpdateDestroyAPIView.as_view,
        create_update_serializer_class=serializers.TagCreateUpdateSerializer,
        retrieve_serializer_class=serializers.TagRetrieveSerializer,
        service=tag_service,
    )
