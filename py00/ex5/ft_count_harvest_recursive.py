def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))

    def helper(current_day):
        if (current_day > days):
            print("Harvest time!")
            return
        print(f"Day {current_day}")
        helper(current_day + 1)
    helper(1)
