import sys
import json


def solve(authors):
    def h_index(publications):
        citations = list(
            enumerate(sorted(publications.values(), reverse=True), 1))
        h_index = 0
        for citation in citations:
            h_index, number_of_citations = citation
            if h_index > number_of_citations:
                h_index -= 1
                break
        return h_index

    result = []
    for author, publications in authors.items():
        result.append((author, h_index(publications)))

    return sorted(result, key=lambda a: (-a[1], a[0]))


def read_data():
    number_of_records = int(input())
    result = {}
    for _ in range(number_of_records):
        publication = json.loads(input())
        citing_paper_count = publication['citing_paper_count']
        publication_number = publication['article_number']
        authors = publication['authors']['authors']
        for author in authors:
            author_full_name = author['full_name']
            if author_full_name not in result:
                result[author_full_name] = {}
            result[author_full_name][publication_number] = citing_paper_count
    return result


def main():
    authors = read_data()
    result = solve(authors)
    for name, h_index in result:
        print(name, h_index)


if __name__ == '__main__':
    # sys.stdin = open('input.txt')
    main()
