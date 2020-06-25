class Tree():
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    @classmethod
    def insert(cls, tree, value, infix=''):
        if tree.value is None:
            tree.value = value
        else:
            node = Tree(value)
            if infix.find(value) < infix.find(tree.value):
                if tree.left is None:
                    tree.left = node
                else:
                    cls.insert(tree.left, value, infix=infix)
            else:
                if tree.right is None:
                    tree.right = node
                else:
                    cls.insert(tree.right, value, infix=infix)

    @classmethod
    def get_level(cls, tree, level, visited_nodes):
        if level == 0:
            visited_nodes.append(str(tree.value))
        else:
            if tree.left is None:
                cls.get_level(Tree('-'), level-1, visited_nodes)
            else:
                cls.get_level(tree.left, level-1, visited_nodes)
            if tree.right is None:
                cls.get_level(Tree('-'), level-1, visited_nodes)
            else:
                cls.get_level(tree.right, level-1, visited_nodes)

    @classmethod
    def get_all_levels(cls, tree):
        data = []
        level_counter = 0
        while True:
            level_elements = []
            Tree.get_level(tree, level_counter, level_elements)
            if level_elements.count('-') == len(level_elements):
                break
            else:
                data.append(level_elements.copy())
                level_counter += 1
        return data

    @classmethod
    def print(cls, tree):
        current_steps = 0
        result = []
        levels = cls.get_all_levels(tree)
        left_margin = 1000

        for level in levels[::-1]:
            next_steps = current_steps*2+1
            result.append('{}{}'.format(current_steps*'-',
                                        (next_steps*'-').join(level)))
            current_steps = next_steps

        for level in result:
            for index in range(len(level)):
                if level[index] != '-':
                    if index < left_margin:
                        left_margin = index
                    break

        for n in result[::-1]:
            print(n[left_margin:].replace('-', ' '))

    @classmethod
    def generate_tree(cls, infix, prefix):
        tree = Tree()
        for element in prefix:
            Tree.insert(tree, element, infix=infix)
        return tree


def solve(infix, prefix):
    tree = Tree.generate_tree(infix, prefix)
    Tree.print(tree)


def main():
    while True:
        try:
            infix = input()
            prefix = input()
            solve(infix, prefix)
        except EOFError:
            break


if __name__ == '__main__':
    main()
