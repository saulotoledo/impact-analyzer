from dependency_injector import containers, providers
from tags.containers import TagsContainer
from tables.containers import TablesContainer
from . import settings


class Container(containers.DeclarativeContainer):

    config = providers.Configuration()

    tags_package = providers.Container(
        TagsContainer
    )

    tables_package = providers.Container(
        TablesContainer
    )

def get_container():
    container = Container()
    container.config.from_dict(settings.__dict__)
    return container
