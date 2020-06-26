import json


def read_data():
    number_of_records = int(input())-1
    publications_to_report = json.loads(input())['publications']
    publications_to_analyze = []
    for _ in range(number_of_records):
        publications_to_analyze.append(json.loads(input()))
    return publications_to_report, publications_to_analyze


def solve(publications_to_report, publications_to_analyze):
    def get_publications(publications_to_report):
        result = {}
        for publication in publications_to_report:
            counter = 0
            for article in publication['articleCounts']:
                if article['year'] in ('2017', '2018'):
                    counter += int(article["articleCount"])
            result[publication['publicationNumber']] = counter
        return result

    def get_citations(publication_numbers, publications_to_analyze):
        result = {}
        for publication in publications_to_analyze:
            cited_articles = publication['paperCitations']['ieee']
            for article in cited_articles:
                if (article['publicationNumber'] in publication_numbers
                        and article['year'] in ('2017', '2018')):
                    result[article['publicationNumber']] = result.get(
                        article['publicationNumber'], 0) + 1
        return result

    def get_publications_info(publications_to_report):
        result = dict()
        for publication in publications_to_report:
            result[publication['publicationNumber']] =\
                publication['publicationTitle']
        return result

    publications_info = get_publications_info(publications_to_report)
    publication_numbers = publications_info.keys()
    total_publications = get_publications(publications_to_report)
    total_citations = get_citations(
        publication_numbers, publications_to_analyze)

    result = {}

    for publication_number in publication_numbers:
        publications = total_publications[publication_number]
        citations = total_citations[publication_number]
        impact_factor = citations/publications
        result[publications_info[publication_number]] = impact_factor

    return sorted(result.items(), key=lambda a: (-a[1], a[0]))


def main():
    publications_to_report, publications_to_analyze = read_data()
    result = solve(publications_to_report, publications_to_analyze)
    for item in result:
        title, impact_factor = item
        auxiliar = impact_factor
        print('{}: {}'.format(title, '%.2f' % round(impact_factor, 2)))


if __name__ == '__main__':
    main()
