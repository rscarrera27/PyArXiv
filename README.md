# pyArXiv(improved_arxiv) ![License](https://img.shields.io/badge/License-bbakbbak2-blue.svg)

improved ArXiv downloader that changes pdf name into real paper name.  

1506.01497.pdf ==> Faster_R-CNN__Towards_Real-Time_Object_Detection_with_Region_Proposal__Networks.pdf


https://pypi.python.org/pypi/improved-ArXiv

```
pip install improved-arxiv
```

below code is example use.
```python
from improved_arxiv.pyArXiv import pyArXiv  

paper_id = 1506.01497  # example id

paper_info = pyArXiv.query(paper_id)
pyArXiv.download(paper_info)
```