import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-slick',
    version='0.1',
    packages=['slick'],
    include_package_data=True,
    license='MIT License',  # example license
    description='A simple Django app to construct galleries and sliders.',
    long_description=README,
    url='https://github.com/Carioca/django_slick/',
    author='Marcelo Gasparian Gosling',
    author_email='slick@ex.ato.br',
    install_requires = [
        #'pillow',
        #'sorl-thumbnail',
        'django-admin-sortable2',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License', # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
