from setuptools import setup

setup(
    name='lektor-markdown-admonition',
    description='Adds basic admonition tag support to Markdown.',
    version='0.1',
    author=u'Armin Ronacher',
    author_email='armin.ronacher@active-4.com',
    url='http://github.com/lektor/lektor-markdown-admonition',
    license='BSD',
    py_modules=['lektor_markdown_admonition'],
    entry_points={
        'lektor.plugins': [
            'markdown-admonition = lektor_markdown_admonition:MarkdownAdmonitionPlugin',
        ]
    }
)
