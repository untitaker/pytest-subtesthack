from setuptools import setup

setup(
    name='pytest-subtesthack',
    description='A hack to explicitly set up and tear down fixtures.',
    long_description=open('README.rst').read(),
    version='0.1.2',
    license='Public domain',
    author='Markus Unterwaditzer',
    author_email='markus@unterwaditzer.net',
    url='https://github.com/untitaker/pytest-subtesthack/',
    py_modules=['pytest_subtesthack'],
    entry_points={'pytest11': ['subtesthack = pytest_subtesthack']},
    install_requires=['pytest']
)
