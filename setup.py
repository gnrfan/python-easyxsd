from setuptools import setup

description = 'Easy XML Schema Definition (XSD) validation of XML documents'

try:
    with open('README.md') as f:
        long_description = f.read()
except IOError:
    long_description = description

setup(
    name = 'easyxsd',
    version = '0.1',
    description = description,
    author = 'Antonio Ognio',
    author_email = 'antonio@ognio.com',
    url = 'https://github.com/gnrfan/python-easyxsd',
    long_description = long_description,
    packages = ['easyxsd'],
    install_requires = ['lxml >= 3.3.5'],
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
