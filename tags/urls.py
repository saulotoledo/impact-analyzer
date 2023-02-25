from django.urls import path
from impact_analyzer.containers import get_container


# TODO: Investigate why we cannot initialize the container at the __init__.py
# The documentation for the dependency-injector library suggests initializing
# the container at the __init__.py file. However, that leads to the exception
# "django.core.exceptions.AppRegistryNotReady" when using the MP_Node module
# in our models. Therefore, we initialize the container here. We should
# investigate the reasons for this behavior and review our settings.

container = get_container().tags_package.container

urlpatterns = [
    path('', container.tag_list_create_api_view(), name='tag-list-create'),
    path('<int:id>/', container.tag_retrieve_update_destroy_api_view(), name='tag-retrieve-update-destroy'),
]
