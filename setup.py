from setuptools import setup, find_packages
from os import path
from starred import VERSION


this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md')) as f:
    long_description = f.read()


setup(
    name='starred',
    version=VERSION,
    url='https://github.com/yrqgithub/starred',
    license='MIT',
    author='yrqgithub',
    author_email='',
    keywords='GitHub starred',
    description='creating your own Awesome List used GitHub stars!',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    platforms='any',
    python_requires='>=3.6',
    install_requires=[
        'click==7.1.2',
        'github3.py==1.3.0',
    ],
    entry_points={
        'console_scripts': [
            'starred=starred.starred:starred'
        ]
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
