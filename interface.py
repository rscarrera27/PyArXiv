from improved_arxiv.pyArXiv import pyArXiv

print("Thanks for using pyArXiv!\n\n")
paper_id = input("paper id : ")
paper_info = pyArXiv.query(paper_id)
print(paper_info)
pyArXiv.download(paper_info)