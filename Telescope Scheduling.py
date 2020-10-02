import sys


def read_data():
    number_of_stars = int(input())
    data = [tuple(map(int, input().split())) for _ in range(number_of_stars)]
    return data


def solve(data):

    def max_desirability(current_element=len(data)-1, used_schedule=set()):
        if current_element == -1:
            return 0
        elif used_schedule.intersection(set(range(data[current_element][0], data[current_element][1]))) != set():
            return max_desirability(current_element-1, used_schedule)
        else:
            auxiliar_a = max_desirability(current_element-1, used_schedule)
            auxiliar_b = data[current_element][2] + max_desirability(current_element-1, used_schedule.union(
                set(range(data[current_element][0], data[current_element][1]))))
            return max(auxiliar_a, auxiliar_b)

    result = max_desirability()
    return result


def main():
    data = read_data()
    result = solve(data)
    print(result)


if __name__ == '__main__':
    sys.stdin = open('input.txt')
    main()
