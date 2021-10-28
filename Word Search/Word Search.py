def main():

    def search_horizontal():
        for row_idx, row in enumerate(grid):
            rs = row_idx
            for word in words:
                cs = row.find(word)
                if cs != -1:
                    cs -= r - 1
                    results[word] = min(results[word], (rs, cs, rs, cs - 1 + len(word)))

                ce = row.find(word[::-1])
                if ce != -1:
                    ce -= r-1
                    results[word] = min(results[word], (rs, ce - 1 + len(word), rs, ce))

    def search_vertical():
        for col_idx in range(r-1, c+r-1):
            cs = col_idx - (r-1)
            col = ''.join([row[col_idx] for row in grid])
            for word in words:
                rs = col.find(word)
                if rs != -1:
                    results[word] = min(results[word], (rs, cs, rs - 1 + len(word), cs))

                re = col.find(word[::-1])
                if re != -1:
                    results[word] = min(results[word], (re - 1 + len(word), cs, re, cs))

    def search_diagonal_up():
        for col_idx in range(0, c + r - 1):
            diagonal = ''.join([grid[row_idx][col_idx + (r - 1 - row_idx)] for row_idx in range(r - 1, -1, -1)])
            for word in words:
                rs = diagonal.find(word)
                if rs != -1:
                    cs = rs + col_idx - (r - 1)
                    rs = r - rs - 1
                    results[word] = min(results[word], (rs, cs, rs + 1 - len(word), cs - 1 + len(word)))

                re = diagonal.find(word[::-1])
                if re != -1:
                    ce = re + col_idx - (r - 1)
                    re = r - re - 1
                    results[word] = min(results[word], (re + 1 - len(word), ce - 1 + len(word), re, ce))

    def search_diagonal_down():
        for col_idx in range(0, c + r - 1):
            diagonal = ''.join([grid[row_idx][col_idx + row_idx] for row_idx in range(r)])
            for word in words:
                rs = diagonal.find(word)
                if rs != -1:
                    cs = rs + col_idx - (r - 1)
                    results[word] = min(results[word], (rs, cs, rs - 1 + len(word), cs - 1 + len(word)))

                re = diagonal.find(word[::-1])
                if re != -1:
                    ce = re + col_idx - (r - 1)
                    results[word] = min(results[word], (re - 1 + len(word), ce - 1 + len(word), re, ce))

    r, c, q = map(int, input().split())
    default_result = (1000, 1000, 1000, 1000)
    grid = []
    results = {}
    words = []

    for _ in range(r):
        grid.append((r-1)*'.' + input() + (r-1)*'.')

    for _ in range(q):
        word = input()
        words.append(word)
        results[word] = default_result

    search_horizontal()
    search_vertical()
    search_diagonal_down()
    search_diagonal_up()

    for word in words:
        result = results[word]
        if result == default_result:
            print(-1)
        else:
            print(*result)


if __name__ == '__main__':
    main()
