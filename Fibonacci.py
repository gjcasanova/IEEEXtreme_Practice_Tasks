last_digits = [1, 1, 2, 3, 5, 8, 3, 1, 4, 5, 9, 4, 3, 7, 0, 7, 7, 4, 1, 5, 6,
               1, 7, 8, 5, 3, 8, 1, 9, 0, 9, 9, 8, 7, 5, 2, 7, 9, 6, 5, 1,
               6, 7, 3, 0, 3, 3, 6, 9, 5, 4, 9, 3, 2, 5, 7, 2, 9, 1, 0, 1]


def input_data():
    numbers = []
    number_of_cases = int(input())
    for _ in range(number_of_cases):
        number = int(input())
        numbers.append(number)
    return numbers


def main():
    numbers = input_data()
    for number in numbers:
        print(last_digits[number % 60])


if __name__ == '__main__':
    main()
