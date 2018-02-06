import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='wagtail-paginated-subpages',
    version='0.6.1',
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',
    description='A pagination plugin app for django wagtail CMS',
    long_description=README,
    url='https://github.com/Designer023/Wagtail-Paginated-Subpages',
    author='Carl Topham',
    author_email='carl@carl-topham.com',
    install_requires=[
        'django>=1.11,<1.12',
        'wagtail>=1.13,<1.14'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
