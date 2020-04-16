def resolve(elements):

    def search_node(nodes, value):
        result = tuple()
        for node in nodes:
            if node[0][0] < value <= node[0][1]:
                result = node
                nodes.remove(result)
                return result

    nodes = [((float('-Inf'), float('Inf')), 1)]

    for element in elements:
        node = search_node(nodes, element)
        ((left, right), level) = node
        nodes.insert(0, ((left, element), level + 1))
        nodes.insert(1, ((element, right), level + 1))
        print(level, end=' ')


def main():
    number_of_elements = int(input())
    elements = map(int, input().split())
    resolve(elements)


if __name__ == '__main__':
    main()
