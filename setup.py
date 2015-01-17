from setuptools import setup, find_packages

setup(
    name='requests-cloudauth',
    version='0.0.1',
    description=(''),
    long_description=(''),
    url='https://github.com/jmvrbanac/requests-cloud-auth',
    author='John Vrbanac',
    author_email='john.vrbanac@linux.com',
    license='Apache v2',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2.7',
    ],

    keywords='',
    packages=find_packages(exclude=['contrib', 'docs', 'spec*']),
    install_requires=['requests>=2.4.1'],
    package_data={},
    data_files=[],
    entry_points={
        'console_scripts': [],
    },
)
