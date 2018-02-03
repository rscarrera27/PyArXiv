from bs4 import BeautifulSoup
import requests
import urllib.request


class Paper:

    def __init__(self, paper_name, paper_id, authors, abstract):
        self.paper_name = paper_name
        self.paper_id = paper_id
        self.authors = authors
        self.abstract = abstract

    def download(self):
        url = "https://arxiv.org/pdf/{}.pdf".format(self.paper_id)
        pdf_name = "{}.pdf".format(self.paper_name).replace(' ', '_').replace(':', '')

        urllib.request.urlretrieve(url, "{}".format(pdf_name))


class ArXiv:


    @staticmethod
    def download(paper):
        paper.download()

    @staticmethod
    def query(paper_id):

        """
        :param paper_id: int
        :return: {
                  "paper_id": int,
                  "paper_name": str
                  }
        """
        url = "https://arxiv.org/abs/{}".format(paper_id)
        html = requests.get(url)

        if html.status_code != 200:
            return ValueError

        html = BeautifulSoup(html.text, 'html.parser')

        paper_name = str(list(html.find("h1", "title mathjax"))[1])[1:]
        authors = [name.text for name in html.find("div", "authors").find_all("a")]
        abstract = str(list(html.find("blockquote", "abstract mathjax"))[2])

        paper = Paper(paper_name=paper_name,
                      paper_id=paper_id,
                      authors=authors,
                      abstract=abstract)

        return paper