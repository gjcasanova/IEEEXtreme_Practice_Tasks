def main():
    number_of_cases = int(input())
    for _ in range(number_of_cases):
        gadgets = {0: 0}
        max_capacity, number_of_gadgets = map(int, input().split())
        for __ in range(number_of_gadgets):
            weight, power = map(int, input().split())
            for element in gadgets.copy().items():
                acumulate_weight = weight + element[0]
                acumulate_power = power + element[1]
                if acumulate_weight <= max_capacity:
                    if acumulate_weight in gadgets:
                        gadgets[acumulate_weight] = max(
                            gadgets[acumulate_weight], acumulate_power)
                    else:
                        gadgets[acumulate_weight] = acumulate_power
        print(max(map(lambda n: n[1], gadgets.items())))


if __name__ == '__main__':
    main()
