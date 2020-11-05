import math


def main():
    c, n, p, w = map(int, input().split())

    if (c >= p or c * n >= w):
        result = w // c
    else:
        result = n-math.ceil((w-c*n)/(p-c))

    print(result)


if __name__ == '__main__':
    main()
