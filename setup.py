from setuptools import setup, find_packages

setup(
    name='improved_ArXiv',
    version='0.0.3',
    description='ArXiv paper downloader',
    license='bbakbbak2',
    author='Lewis Kim',
    author_email='artoria@istruly.sexy',
    url='https://github.com/devArtoria/pyArXiv',
    keywords=['ArXiv', 'parsing', 'downloader'],
    install_requires=[],
    packages=find_packages(exclude=['tests', 'interface.py']),
    zip_safe=False,
    requires=[
        "requests",
        "bs4"
    ]
)