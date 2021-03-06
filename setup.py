import os
from setuptools import setup

setup(
    name='django-rest-authemail-anglus',
    version='0.1.5',
    author='Celia Oakley',
    author_email='celia.oakley@alumni.stanford.edu',
    description='A RESTful API for user signup and authentication using email addresses. Forked by Anglus',
    keywords=[
        'django', 'python', 'rest', 'rest-framework', 'api', 
        'auth', 'authentication', 'email', 'user', 'username', 
        'registration', 'signup', 'login', 'logout', 'password',
        'django-rest-framework', 'djangorestframework', 'django-registration', 
        'django-email-as-username'
    ],
    url='http://github.com/celiao/django-rest-authemail',
    download_url='https://github.com/celiao/django-rest-authemail/tarball/0.1.4',
    license='GPLv3 licence, see LICENSE file',
    packages=['authemail'],
    include_package_data=True,
    long_description=open('README.rst').read(),
    install_requires=[
        'Django==1.7.1',
        'djangorestframework==2.4.3',
        'requests>=2.3.0',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development',
        'Topic :: Utilities',
    ],
)
