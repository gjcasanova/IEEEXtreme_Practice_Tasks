def solve(performance_indexes, team_performance_index):
    def get_zero_indexes(number):
        result = []
        index_counter = 0
        while number != 0:
            if number % 2 == 0:
                result.append(index_counter)
            number = number >> 1
            index_counter += 1
        return result

    def is_valid(indexes, number):
        for index in zero_indexes:
            if (number >> index) % 2 == 1:
                return False
        return True

    result = 0
    zero_indexes = get_zero_indexes(team_performance_index)

    for zero_index in performance_indexes:
        if zero_index <= team_performance_index and is_valid(zero_indexes, zero_index):
            result = result | zero_index

        if result == team_performance_index:
            return 'YES'

    return 'NO'


def main():
    number_of_players = int(input())
    performance_indices = list(map(int, input().split()))
    number_of_queries = int(input())
    for _ in range(number_of_queries):
        team_performance_index = int(input())
        result = solve(performance_indices, team_performance_index)
        print(result)


if __name__ == '__main__':
    main()
