from bs4 import BeautifulSoup
import requests
import urllib.request


class pyArXiv:

    def __init__(self):
        pass

    @staticmethod
    def download(paper_info):

        """
        :param paper_info: {
                            "paper_id": int,
                            "paper_name": str
                            }
        :return: None
        """
        paper_name = paper_info["paper_name"][1:]  # remove newline character by str slicing
        paper_id = paper_info["paper_id"]

        url = "https://arxiv.org/pdf/{}.pdf".format(paper_id)
        pdf_name = "{}.pdf".format(paper_name).replace(' ', '_')

        urllib.request.urlretrieve(url, "{}".format(pdf_name))  # TODO: directory select feature

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

        paper_name = str(list(BeautifulSoup(html.text, 'html.parser').find("h1", "title mathjax"))[1])

        paper_info = {
            "paper_id": paper_id,
            "paper_name": paper_name
        }

        return paper_info