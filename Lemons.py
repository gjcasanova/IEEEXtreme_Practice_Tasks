import math


def resolve(pumps, travel_time, check_time):
    def calculate_checks(pumps):
        result = 0
        while pumps != 1:
            pumps = math.ceil(pumps/2)
            result += 1
        return result

    return (pumps-1)*travel_time + calculate_checks(pumps)*check_time


def main():
    pumps, travel_time, check_time = map(int, input().split())
    print(resolve(pumps, travel_time, check_time))


if __name__ == "__main__":
    main()
