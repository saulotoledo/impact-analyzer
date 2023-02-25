from dependency_injector import containers, providers
from tags.containers import TagsContainer
from . import settings


class Container(containers.DeclarativeContainer):

    config = providers.Configuration()

    tags_package = providers.Container(
        TagsContainer
    )


def get_container():
    container = Container()
    container.config.from_dict(settings.__dict__)
    return container
