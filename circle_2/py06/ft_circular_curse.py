"""Part IV"""

from alchemy.grimoire import record_spell as rec
from alchemy.grimoire import validate_ingredients as val

print("\n=== Circular Curse Breaking ===")

print("\nTesting ingredient validation:")
print(f'validate_ingredients("fire"): {val("fire")}')
print(f'validate_ingredients("dragon scales"): {val("dragon")}')

print("\nTesting spell recording with validation:")
print(f'record_spell("Fireball", "fire"): {rec("Fireball", "fire")}')
print(f'record_spell("Dark Magic", "shadow"): {rec("Dark Magic", "shadow")}')

print("\nTesting late import technique:")
print(f'record_spell("Lightning", "air"): {rec("Lightning", "air")}')

print("\nCircular dependency curse avoided using late imports!")
print("All spells processed safely!")
