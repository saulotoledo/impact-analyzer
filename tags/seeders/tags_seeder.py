from tags.models import Tag

def seed_tags_table():
    env_impact = Tag.add_root(name='Environmental impact')
    air_polution = env_impact.add_child(name='Air polution')
    air_polution.add_child(name='Polution by nitrogen dioxide')
    air_polution.add_child(name='Polution by particulate matter')
    air_polution.add_child(name='Polution by sulphur dioxide')
    env_impact.add_child(name='Deforestation')
    env_impact.add_child(name='Land polution')

    env_change = Tag.add_root(name='Environmental change')
    env_change.add_child(name='Climate change')
    env_change.add_child(name='Freshwater shortage')
    env_change.add_child(name='Loss of biodiversity')

    advantages = Tag.add_root(name='Advantages')
    advantages.add_child(name='Flexibility')
    advantages.add_child(name='Freedom')
    advantages.add_child(name='Independence')
    advantages.add_child(name='Safety')
