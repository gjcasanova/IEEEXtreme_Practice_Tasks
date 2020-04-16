def resolve(number_of_pairs):
    def find(key, iterable, index=0):
        for element in iterable:
            if element[index] == key:
                return element
        else:
            return -1

    matched_indexes, flipped_cards = [], []
    index_i = 1
    while index_i < number_of_pairs*2:
        if index_i in matched_indexes:
            index_i += 1
            continue
        else:
            index_j = index_i + 1
            while index_j <= number_of_pairs*2:
                if index_j in matched_indexes:
                    index_j += 1
                    continue
                else:
                    print(index_i, index_j)
                    feedback = input()
                    if feedback == 'MATCH':
                        matched_indexes.append(index_i)
                        matched_indexes.append(index_j)
                    else:
                        card_a, card_b = map(int, feedback.split())
                        search_result = find(card_a, flipped_cards, 1)
                        if search_result != -1:
                            matched_indexes.append(index_i)
                            matched_indexes.append(search_result[0])
                            flipped_cards.remove(search_result)
                            print(search_result[0], index_i)
                            input()
                        else:
                            flipped_cards.append((index_i, card_a))

                        search_result = find(card_b, flipped_cards, 1)
                        if search_result != -1:
                            matched_indexes.append(index_j)
                            matched_indexes.append(search_result[0])
                            flipped_cards.remove(search_result)
                            print(search_result[0], index_j)
                            input()
                        else:
                            flipped_cards.append((index_j, card_b))
                break
        index_i += 2
    else:
        print(-1)


def main():
    number_of_pairs = int(input())
    resolve(number_of_pairs)


if __name__ == '__main__':
    main()
