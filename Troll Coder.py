def change_bit(bit):
    return '1' if bit == '0' else '0'


def print_query(sequence, letter):
    print('{} {}'.format(letter, ' '.join(sequence)))


def input_data():
    length = int(input())
    return length*['0']


def main():
    sequence = input_data()
    print_query(sequence, 'Q')
    correct_bits = auxiliar_correct_bits = int(input())
    index = 0
    while(correct_bits != len(sequence)):
        sequence[index] = change_bit(sequence[index])
        print_query(sequence, 'Q')
        correct_bits = int(input())
        if correct_bits < auxiliar_correct_bits:
            sequence[index] = change_bit(sequence[index])
            correct_bits = auxiliar_correct_bits
        auxiliar_correct_bits = correct_bits
        index += 1

    print_query(sequence, 'A')


if __name__ == "__main__":
    main()
