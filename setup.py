import ast
import io
import re

from setuptools import setup, find_packages

with io.open('README.md', 'rt', encoding="utf8") as f:
    readme = f.read()

_description_re = re.compile(r'description\s+=\s+(?P<description>.*)')

with open('lektor_force_update.py', 'rb') as f:
    description = str(ast.literal_eval(_description_re.search(
        f.read().decode('utf-8')).group(1)))

setup(
    author=u'relikd',
    author_email='oleg@relikd.de',
    description=description,
    keywords='Lektor plugin force cache appcache rebuild build',
    license='MIT',
    long_description=readme,
    long_description_content_type='text/markdown',
    name='lektor-force-update',
    packages=find_packages(),
    py_modules=['lektor_force_update'],
    url='https://github.com/relikd/lektor-force-update-plugin',
    version='1.0',
    classifiers=[
        'Framework :: Lektor',
        'Environment :: Plugins',
    ],
    entry_points={
        'lektor.plugins': [
            'force-update = lektor_force_update:ForceUpdatePlugin',
        ]
    }
)
