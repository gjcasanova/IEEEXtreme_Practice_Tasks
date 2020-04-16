import sys
sys.setrecursionlimit(1500)


def resolve(elements, result={}):
    def get_childs(reference, elements):
        minor_childs, major_childs = [], []
        for element in elements:
            if element <= reference:
                minor_childs.append(element)
            else:
                major_childs.append(element)
        return minor_childs, major_childs

    def travel(elements, result, level=1):
        if not elements:
            return
        else:
            current = elements.pop(0)
            if current in result:
                result[current].append(level)
            else:
                result[current] = [level]
            minor_childs, major_childs = get_childs(current, elements)
            travel(minor_childs, result, level+1)
            travel(major_childs, result, level+1)

    def show_result(elements, result):
        for element in elements:
            print(result[element].pop(0), end=' ')

    travel(elements.copy(), result)
    show_result(elements, result)


def main():
    number_of_elements = int(input())
    elements = list(map(int, input().split()))
    resolve(elements)


if __name__ == '__main__':
    sys.stdin = open('input.txt')
    main()
