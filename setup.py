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
    version='1.0.7',
    description='An automation tool to control GitHub, using the developers terminal with cool automation',
    long_description=readme(),
    long_description_content_type="text/markdown",
    author='GN Vageesh',
    author_email='vageeshgn2005@gmail.com',
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python :: 3",
        'Environment :: Console',
        'Development Status :: 5 - Production/Stable'
    ],
    license='MIT',
    keywords=['python', 'python3', 'automation',
              'console', 'click', 'selenium', 'easy', 'hacks', 'cli'],
    maintainer='GN Vageesh',
    maintainer_email='vageeshgn2005@gmail.com',
    download_url='https://github.com/GNVageesh/gnv',
    packages=find_packages(),
    include_package_data=True,
    install_requires=read_requirements(),
    url="https://pypi.org/project/gnv/",
    entry_points='''
        [console_scripts]
        gnv=gnv.cli:cli
    '''
)
