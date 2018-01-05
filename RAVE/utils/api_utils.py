import requests


def get_search_results(param):
    payload = {'search': param}
    r = requests.get("https://en.wikipedia.org/w/api.php?action=opensearch&format=json&namespace=0%7C14&limit=10",
                     params=payload)
    if r.status_code == 200:
        search_results = r.json()
        s = search_results[1]
        return s


def get_wiki_page(param):
    payload = {'page': param}
    r = requests.get('https://en.wikipedia.org/w/api.php?action=parse&format=json&prop=text&disableeditsection=1', params=payload)
    # /w/api.php?action=parse&format=json&page=Cubism&prop=text%7Cimages&disableeditsection=1&contentmodel=wikitext
    # https://en.wikipedia.org/w/api.php?action=parse&format=json&page=Modena&prop=text&wrapoutputclass=mw-parser-output&utf8=1
    # decoding json
    if r.status_code == 200:
        data = r.json()
        # accessing the html code
        wiki_html = data['parse']['text']['*']

        return wiki_html


"""
def get_wiki_page(param):

    payload = {'page': param}
    r = requests.get('https://en.wikipedia.org/w/api.php?action=parse&format=json&prop=text', params=payload)
    # https://en.wikipedia.org/w/api.php?action=parse&format=json&page=Modena&prop=text&wrapoutputclass=mw-parser-output&utf8=1
    # decoding json
    if r.status_code == 200:

        data = r.json()
        # accessing the html code
        wiki_html = data['parse']['text']['*']

        # prettify the html data. Optional.
        # TODO https://stackoverflow.com/questions/15059206/how-should-i-populate-json-data-in-a-django-template
        # TODO https://duckduckgo.com/?q=jquery+append+html+to+div+json&t=ffab&ia=qa
        soup = BeautifulSoup(wiki_html, "html5lib")
        pretty_soup = soup.div.prettify(formatter="html", encoding="utf-8")
        return pretty_soup
"""