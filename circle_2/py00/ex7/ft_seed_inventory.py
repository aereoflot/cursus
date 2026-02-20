def ft_seed_inventory(seed_type, quantity, unit):
    if (unit == "packets"):
        print(f"{seed_type.capitalize()} seed: {quantity} {unit} aviable")
    elif (unit == "grams"):
        print(f"{seed_type.capitalize()} seeds: {quantity} {unit} total")
    elif (unit == "area"):
        print(f"{seed_type.capitalize()} seeds: \
            covers {quantity} square meters")
    else:
        print("Unknown unit type")
