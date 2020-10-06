def flatten(array):
    result = []
    for element in array:
        if type(element) == int:
            result.append(str(element))
        else:
            for subelement in element:
                result.append(str(subelement))
    return result


def get_min_values(array, max_value):
    for index in range(len(array)):
        if array[index] > max_value:
            return array[:index], array[index:]
    return array, []


def get_max_values(array, min_value):
    for index in range(len(array)):
        if array[index] > min_value:
            return array[index:], array[:index]
    return [], array


def merge(base_array, insert_array):
    insert_array.sort()
    # Initial insertion
    values_to_insert, insert_array = get_min_values(
        insert_array, base_array[0])
    base_array = values_to_insert + base_array
    counter = len(values_to_insert)
    # Final insertion
    values_to_insert, insert_array = get_max_values(
        insert_array, max(base_array))
    base_array.extend(values_to_insert)
    auxiliar_limit = len(values_to_insert)
    # Intermedial insertion

    while counter < len(base_array)-auxiliar_limit:
        limit_inf, limit_sup = base_array[counter-1], base_array[counter]
        if limit_sup > limit_inf+1:
            values_to_insert, insert_array = get_min_values(
                insert_array, limit_sup)
            base_array.insert(counter, values_to_insert)
            if len(insert_array) == 0:
                break
            else:
                counter += 1
        counter += 1
    return flatten(base_array)


def input_data():
    input()
    auxiliar_input = input().split()
    base_array = [int(number) for number in auxiliar_input]
    auxiliar_input = input().split()
    insert_array = [int(number) for number in auxiliar_input]
    return base_array, insert_array


def main():
    base_array, insert_array = input_data()
    result = merge(base_array, insert_array)
    print(' '.join(result))


if __name__ == '__main__':
    main()
