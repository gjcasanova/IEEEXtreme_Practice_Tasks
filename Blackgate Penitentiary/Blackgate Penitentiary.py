import collections


def input_data():
    members_data = dict()
    number_of_cases = int(input())
    for case in range(number_of_cases):
        member_data = input().split()
        if int(member_data[1]) in members_data:
            members_data.get(int(member_data[1])).append(member_data[0])
            members_data.get(int(member_data[1])).sort()
        else:
            members_data.update({int(member_data[1]): [member_data[0]]})
    return collections.OrderedDict(sorted(members_data.items()))


def main():
    members_data = input_data()
    counter = 1
    for key, value in members_data.items():
        print('{} {} {}'.format(' '.join(value), counter,
                                counter + len(value) - 1))
        counter += len(value)


if __name__ == '__main__':
    main()
