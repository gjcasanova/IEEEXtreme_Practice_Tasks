import numpy as np

visited_nodes = []


def search_cycles(adjacency_matrix, current, pre=None):
    visited_nodes.append(current)
    destinies = np.where(adjacency_matrix[current] == 1)[0]
    for destiny in destinies:
        if destiny != pre:
            if (destiny in visited_nodes
                    or search_cycles(adjacency_matrix, destiny, current)):
                return 1
    else:
        return 0


def input_data():
    data = []
    number_of_cases = int(input())
    for _ in range(number_of_cases):
        auxiliar_input = input().split()
        number_of_vertex, number_of_edges = int(
            auxiliar_input[0]), int(auxiliar_input[1])
        auxiliar_data = input().split()
        adjacency_matrix = np.zeros(
            (number_of_vertex, number_of_vertex), dtype=int)
        nodes = [int(number) for number in auxiliar_data]
        for index in range(0, len(nodes)-1, 2):
            origin, destiny = nodes[index], nodes[index+1]
            adjacency_matrix[origin][destiny] = 1
            adjacency_matrix[destiny][origin] = 1
        data.append(adjacency_matrix)

    return data


def main():
    data = input_data()
    for case in data:
        for iterator in range(case.shape[0]):
            visited_nodes.clear()
            if search_cycles(case.copy(), iterator):
                print(1)
                break
        else:
            print(0)


if __name__ == '__main__':
    main()
