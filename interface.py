from improved_arxiv.pyArXiv import ArXiv

print("Thanks for using pyArXiv!\n\n")
paper_id = input("paper id : ")
paper = ArXiv.query(paper_id)
print(paper.paper_id, end='\n\n')
print(paper.paper_name, end='\n\n')
print(paper.authors, end='\n\n')
print(paper.abstract, end='\n\n')
paper.download()
print("download finished")
