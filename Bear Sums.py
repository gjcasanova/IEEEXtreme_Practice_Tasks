def resolve(expected_sum, numbers):
    for index_i in range(1, len(numbers)):
        number_a = numbers[index_i]
        if expected_sum - number_a in numbers[:index_i]:
            print(min(number_a, expected_sum - number_a),
                  max(number_a, expected_sum - number_a))
            break
    else:
        print('!OK')


def main():
    number_of_cases = int(input())
    for _ in range(number_of_cases):
        expected_sum = int(input().split()[0])
        numbers = tuple(map(int, input().split()))
        if len(numbers) > 0:
            min_limit = min(numbers)
            numbers = tuple(n for n in numbers if n <= expected_sum-min_limit)
        resolve(expected_sum, numbers)


if __name__ == '__main__':
    main()
