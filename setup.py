import re
import ast
from setuptools import setup


_version_re = re.compile(r'__version__\s+=\s+(.*)')


with open('click/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))


setup(
    name='plonecli-click',
    author='Maik Derstappen',
    author_email='md@derico.de',
    version=version,
    url='https://github.com/MrTango/click',
    packages=['click'],
    description='A simple wrapper around optparse for '
                'powerful command line utilities.',
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
)
