def solve(pair):
    node_a, node_b = pair
    result = 0
    while node_a != node_b:
        if node_a > node_b:
            node_a //= 2
        else:
            node_b //= 2
        result += 1
    return result


def main():
    number_of_cases = int(input())
    for iterator in range(number_of_cases):
        level_a, level_b = input().split()
        print(solve((int(level_a), int(level_b))))


if __name__ == '__main__':
    main()
