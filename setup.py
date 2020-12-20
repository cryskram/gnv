from setuptools import setup, find_packages


def read_requirements():
    with open('requirements.txt') as rq:
        content = rq.read()
        requirements = content.split('\n')
    return requirements


def readme():
    with open('README.md') as file:
        read = file.read()
    return read


setup(
    name='gnv',
    version='1.0.3',
    description='An automation tool to create and delete GitHub Repos using the developers terminal[in an amazing automated look]',
    long_description=readme(),
    long_description_content_type="text/markdown",
    author='GN Vageesh',
    author_email='vageeshgn2005@gmail.com',
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        'Environment :: Console'
    ],
    license='MIT',
    maintainer='GN Vageesh',
    maintainer_email='vageeshgn2005@gmail.com',
    download_url='https://github.com/GNVageesh/gnv',
    packages=find_packages(),
    keywords='cli',
    include_package_data=True,
    install_requires=read_requirements(),
    url="https://pypi.org/project/gnv/",
    entry_points='''
        [console_scripts]
        gnv=gnv.cli:cli
    '''
)       