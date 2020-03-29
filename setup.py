import setuptools

setuptools.setup(
     name='covid19.py',  
     version='0.0.1',
     author="Alessandro Coppe",
     author_email="",
     description="Track the COVID-19 data in the word from the command line",
     url="https://github.com/alexcoppe/covid19.py",
     packages=["covid19"],
     scripts=["scripts/covid19.py"],
     install_requires=[
          'tabulate'
      ],
     classifiers=[
         "Programming Language :: Python :: 3",
         "Operating System :: OS Independent",
     ],
)
