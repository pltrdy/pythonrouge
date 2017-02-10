from setuptools import setup, find_packages
import pythonrouge
setup(
    name="pythonrouge",
    version=pythonrouge.__version__,
    description="ROUGE script using python",
    url="http://github.com/tagucci/pythonrouge",
    author="tagucci",
    author_email="taguchi.yuya.to0@is.naist.jp",
    keywords=["NL", "CL", "natural language processing", "computational linguistics", "summarization"],
    packages=find_packages(),
    package_data={
        'pythonrouge': ['ROUGE-1.5.5/*.*',
              'ROUGE-1.5.5/XML/*.*',
              'ROUGE-1.5.5/XML/DOM/*.*',
              'ROUGE-1.5.5/XML/Handler/*.*',
              'ROUGE-1.5.5/data/WordNet-2.0.exc.db',
              'ROUGE-1.5.5/data/smart_common_words.txt',
              'ROUGE-1.5.5/data/WordNet-1.6-Exceptions/*.*',
              'ROUGE-1.5.5/data/WordNet-2.0-Exceptions/*.*',
              ],
        },
    classifiers=[
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Topic :: Text Processing :: Linguistic"
        ],
    license="LICENCE.txt",
    long_description=open("README.md").read(),
)
