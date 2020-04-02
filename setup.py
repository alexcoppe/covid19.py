import setuptools


# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
     name='covid19.py',  
     version='0.0.8',
     author="Alessandro Coppe",
     author_email="",
     description="Track the COVID-19 data in the word from the command line",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/alexcoppe/covid19.py",
     scripts=["scripts/covid19.py"],
     install_requires=[
          'tabulate'
      ],
     classifiers=[
         "Programming Language :: Python :: 3",
         "Operating System :: OS Independent",
     ],
)
