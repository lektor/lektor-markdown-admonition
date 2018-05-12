import ast
import io
import re

from setuptools import setup

with io.open('README.md', 'rt', encoding="utf8") as f:
    readme = f.read()

_description_re = re.compile(r'description\s+=\s+(?P<description>.*)')

with open('lektor_markdown_admonition.py', 'rb') as f:
    description = str(ast.literal_eval(_description_re.search(
        f.read().decode('utf-8')).group(1)))

setup(
    author=u'Armin Ronacher',
    author_email='armin.ronacher@active-4.com',
    description=description,
    keywords = 'Lektor plugin markdown admonition static-site blog',
    license='BSD',
    name='lektor-markdown-admonition',
    py_modules=['lektor_markdown_admonition'],
    url='http://github.com/lektor/lektor-markdown-admonition',
    version='0.2',
    classifiers=[
        'Environment :: Plugins',
        'Environment :: Web Environment',
        'Framework :: Lektor',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
    ],
    entry_points={
        'lektor.plugins': [
            'markdown-admonition = lektor_markdown_admonition:MarkdownAdmonitionPlugin',
        ]
    }
)
