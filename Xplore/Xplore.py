import json


def h_index(citations: list):
    citations.sort(reverse=True)
    result = 0

    for h_index, citation in enumerate(citations, start=1):
        if h_index > citation:
            break
        result = h_index

    return result


def main():
    number_of_records = int(input())
    records = {}
    results = []

    for _ in range(number_of_records):
        record = json.loads(input())
        for author in record['authors']['authors']:
            if author['full_name'] in records:
                records[author['full_name']].append(
                    record['citing_paper_count'])
            else:
                records[author['full_name']] = [record['citing_paper_count']]

    for name, citations in records.items():
        results.append((name, h_index(citations)))

    results = sorted(results, key=lambda x: (-x[1], x[0]))

    for result in results:
        print(result[0], result[1])


if __name__ == '__main__':
    main()
