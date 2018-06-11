from setuptools import find_packages
from setuptools import setup


try:
    README = open('README.rst').read() + '\n\n' + open('CHANGELOG.rst').read()
except IOError:
    README = None

setup(
    name='guillotina_prometheus',
    version='1.0.8.dev0',
    description='prometheus integration into guillotina',
    long_description=README,
    install_requires=[
        'guillotina>=2.1.5',
        'prometheus_client'
    ],
    author='Nathan Van Gheem',
    author_email='vangheem@gmail.com',
    url='https://github.com/guillotinaweb/guillotina_prometheus',
    packages=find_packages(exclude=['demo']),
    include_package_data=True,
    tests_require=[
        'pytest',
    ],
    extras_require={
        'test': [
            'pytest'
        ]
    },
    classifiers=[],
    entry_points={
    }
)
