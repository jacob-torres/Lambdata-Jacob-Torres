import setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='Lambdata-Jacob-Torres',
    version='0.0.2',
    author='Jacob Torres',
    author_email='jacob@jacobtorres.net',
    description='A simple python package for manipulating Pandas dataframes.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/jacob-torres/lambdata-jacob-torres/',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7'
)
