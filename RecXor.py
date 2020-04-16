def resolve(width, height, start, diagonal_init, diagonal_finsih):
    def xor(number):
        number -= 1
        case = number % 4
        if case == 0:
            return number
        elif case == 1:
            return 1
        elif case == 2:
            return number+1
        elif case == 3:
            return 0

    def get_points(width, start, diagonal_init, diagonal_finsih):
        point_a = divmod(diagonal_init-start, width)
        point_b = divmod(diagonal_finsih-start, width)
        start_point = (min(point_a[0], point_b[0]),
                       min(point_a[1], point_b[1]))
        end_point = (max(point_a[0], point_b[0]),
                     max(point_a[1], point_b[1]))
        return start_point, end_point

    def get_value(width, start, point):
        number = width*point[0] + point[1] + start
        return number

    internal_xor = 0
    total_xor = xor(width*height+start) ^ xor(start)

    start_point, end_point = get_points(
        width, start, diagonal_init, diagonal_finsih)

    number_of_rows = end_point[0]-start_point[0] + 1
    number_of_columns = end_point[1]-start_point[1] + 1

    init_value = get_value(width, start, start_point)

    for _ in range(number_of_rows):
        internal_xor ^= xor(init_value + number_of_columns) ^ xor(init_value)
        init_value += width

    return total_xor ^ internal_xor


def main():
    number_of_cases = int(input())
    for _ in range(number_of_cases):
        width, height, start, diagonal_init, diagonal_finsih = map(
            int, input().split())
        print(resolve(width, height, start, diagonal_init, diagonal_finsih))


if __name__ == '__main__':
    main()
