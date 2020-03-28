from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='Classifying Personality of a Person Based On Users Twitter Data',
    version='1.3.0',

    install_requires=[ "pandas >= 1.0.2",
			"pickleshare >= 0.7.5",
			"numpy >= 1.17.2",
			"scikit-learn >= 0.21.3",
			"nltk >= 3.4.5",
			"tweepy >= 3.8.0",
			"unicodecsv >= 0.14.1"],

    description='A Natural Language Processing (NLP), Machine Learning and Data Mining project, which will automate the screening process before hiring a professional or can be used in psychiatry to check effectivity of patient therapy.',
    long_description=long_description,


    url='https://github.com/priyansh19/Classification-of-Personality-based-on-Users-Twitter-Data',


    authors = ' Priyansh Gupta, Prakhar Agarwal, Shraddha Saini ',
    author_email='guptapriyansh1907@gmail.com',
    classifiers=[

        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    keywords=' Suggestion Mining using textblob nlp tweepy and nltk',
   
)

