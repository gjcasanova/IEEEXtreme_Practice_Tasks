import math


def solve(alphabet, radius, message):
    def calc_distance(angle_a, angle_b, radius):
        angle = (180-abs(angle_a-angle_b))*math.pi/360
        distance = 2*radius*math.cos(angle)
        return distance

    result = radius
    for index in range(len(message)-1):
        result += calc_distance(alphabet[message[index]],
                                alphabet[message[index+1]], radius)
    return math.ceil(result)


def main():
    def clean_message(message, keys):
        auxiliar_data = [character for character in message.upper()
                         if character in keys]
        result = [auxiliar_data[0]]
        for index in range(1, len(auxiliar_data)):
            if auxiliar_data[index] != result[-1]:
                result.append(auxiliar_data[index].upper())
        return result

    radius = int(input())
    alphabet = {}
    for _ in range(26):
        aux_data = input().split()
        letter, angle = aux_data[0], float(aux_data[1])
        alphabet.update({letter: angle})
    message = clean_message(input(), alphabet.keys())

    print(solve(alphabet, radius, message))


if __name__ == '__main__':
    main()
