def input_data():
    number_of_cases = int(input())
    data = []

    for index in range(number_of_cases):
        data.append((index, int(input())))

    data.sort(key=lambda element: element[1], reverse=True)
    return data


def main():
    position, previous, current = 0, 0, 1
    result = []
    data = input_data()

    while(position <= data[0][1]):
        if position == data[-1][1]:
            result.append((data[-1][0], current))
            data.pop()
            if data == []:
                break
        else:
            auxiliar = current
            current += previous
            previous = auxiliar
            position += 1

    result.sort(key=lambda element: element[0])
    for element in result:
        print(element[1])


if __name__ == '__main__':
    main()
