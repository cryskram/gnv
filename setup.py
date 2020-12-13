from setuptools import setup, find_packages


def read_requirements():
    with open('requirements.txt') as rq:
        content = rq.read()
        requirements = content.split('\n')
    return requirements


setup(
    name='gnv',
    version='1.0.0',
    description='An automation tool to create and delete GitHub Repos using the developers terminal[in an amazing automated look]',
    long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.txt').read(),
    author='GNVageesh',
    author_email='vageeshgn2005@gmail.com',
    url='https://github.com/GNVageesh/gnv',
    license='MIT',
    packages=find_packages(),
    keywords='cli',
    include_package_data=True,
    install_requires=read_requirements(),
    entry_points='''
        [console_scripts]
        gnv=gnv.cli:cli
    '''
)       