
def artifact_sorted(artifacts: list[dict]) -> dict:

    return sorted(artifacts, key=lambda x: x['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:

    return list(filter(lambda ma: ma['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[dict]:

    return list(map(lambda sp: '* '+sp+' *', spells))


def mage_stats(mages: list[dict]) -> dict:

    max_power = max(map(lambda ma: ma['power'], mages))
    min_power = min(map(lambda ma: ma['power'], mages))

    all_power = sum(map(lambda ma: ma['power'], mages))
    avg_power = all_power / len(mages)

    return {"max_power": max_power,
            "min_power": min_power,
            "avg_power": avg_power}


def main():
    artifacts = (
        {'name': 'Earth Shield', 'power': 98, 'type': 'armor'},
        {'name': 'Fire Staff', 'power': 88, 'type': 'focus'},
        {'name': 'Ice Wand', 'power': 75, 'type': 'accessory'}
    )

    print("\nTesting artifact sorter...")

    for artifact in artifact_sorted(artifacts):
        print(artifact['name'] + ",", artifact['power'])

    print("\nTesting power filter...")

    min_power = 80

    print(f"From {len(artifacts)} this are >= {min_power}:")

    if not power_filter(artifacts, min_power):
        print("None")
    else:
        for artifact in power_filter(artifacts, min_power):
            print(f"{artifact['name']}, {artifact['power']}")

    print("\nTesting spell transformer...")

    spells = list(map(lambda arti: arti['name'], artifacts))

    for spell in spell_transformer(spells):
        print(spell)

    print("\nTesting mage stats...")

    stats = mage_stats(artifacts)

    print("max power:", stats['max_power'])
    print("min power:", stats['min_power'])
    print(f"avg of the powers: {stats['avg_power']:.2f}")


if __name__ == "__main__":

    main()
