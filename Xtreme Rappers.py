def order(number_a, number_b):
    if number_a > number_b:
        return number_a, number_b
    return number_b, number_a


def main():
    words = input().split()
    words_a, words_b = order(int(words[0]), int(words[1]))
    total_phrases = 0

    while words_a >= 2 and words_b >= 1:
        if words_a >= 2*words_b:
            total_phrases += words_b
            break
        elif words_a == words_b:
            total_phrases += (2*words_a)//3
            break
        else:
            words_a, words_b = order(words_a-2, words_b-1)
            total_phrases += 1
    print(total_phrases)


if __name__ == '__main__':
    main()
