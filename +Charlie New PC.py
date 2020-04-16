import sys


def input_data():
    prices = []
    budget = int(input())
    number_of_components = int(input())
    input()
    for _ in range(number_of_components):
        option_prices = set(map(int, input().split()))
        prices.append(sorted(option_prices, reverse=True))
    prices.sort(key=len)
    return prices, budget


def resolve(prices, budget):
    def calc_max_price(prices, budget, current=0, acum_price=0):
        if current == len(prices):
            return acum_price
        else:
            max_limit = acum_price + sum(map(lambda n: n[0], prices[current:]))
            if max_limit <= budget:
                return max_limit
            else:
                min_limit = acum_price + \
                    sum(map(lambda n: n[-1], prices[current:]))
                if min_limit > budget:
                    return 0
                else:
                    options = prices[current]
                    result = 0
                    for option in options:
                        auxiliar_price = option + acum_price
                        if auxiliar_price <= budget:
                            auxiliar_result = calc_max_price(
                                prices, budget, current+1, auxiliar_price)
                            if option - budget-auxiliar_result in options:
                                return budget
                            elif auxiliar_result > result:
                                result = auxiliar_result
                    return result

    return calc_max_price(prices, budget)


def main():
    number_of_cases = int(input())
    for _ in range(number_of_cases):
        prices, budget = input_data()
        print(resolve(prices, budget))


if __name__ == '__main__':
    sys.stdin = open('input.txt')
    main()
