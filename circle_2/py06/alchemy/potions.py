
from alchemy import elements


def healing_potion() -> str:
    return f"Healing potion brewed with \
{elements.create_fire()} and {elements.create_water()}"


def strength_potion() -> str:
    return f"Strength potion brewed with \
{elements.create_earth()} and {elements.create_fire()}"


def invisibility_potion() -> str:
    return f"Invisibility potion brewed with \
{elements.create_air()} and {elements.create_water()}"


def wisdom_potion() -> str:
    return f"Wisdom potion brewed with all elements: \
{elements.create_fire()}{elements.create_water()}\
{elements.create_air()}{elements.create_earth()}"
