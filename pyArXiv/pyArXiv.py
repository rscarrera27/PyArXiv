from bs4 import BeautifulSoup
import requests


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
        print(paper_name)

        paper_info = {
            "paper_id": paper_id,
            "paper_name": paper_name
        }

        return paper_info



ad = pyArXiv
ad.query("1412.0035")