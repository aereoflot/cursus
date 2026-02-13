def ft_water_reminder():
    day = int(input("Days since last watring: "))
    if (day > 2):
        print("Water the plants!")
    else:
        print("Plants are fine")
