# pyArXiv(improved_arxiv) ![License](https://img.shields.io/badge/License-bbakbbak2-blue.svg)

improved ArXiv downloader that changes pdf name into real paper name.  

1506.01497.pdf ==> Faster_R-CNN_Towards_Real-Time_Object_Detection_with_Region_Proposal__Networks.pdf


https://pypi.python.org/pypi/improved-ArXiv

```
pip install improved-arxiv
```

below code is example use.
```python
from improved_arxiv.pyArXiv import ArXiv  

paper_id = 1506.01497  # example id

paper = ArXiv.query(paper_id)
paper.download()
```