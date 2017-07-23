from setuptools import setup, find_packages

desc = ''
with open('README.rst') as f:
    desc = f.read()

setup(
    name='requests-cloud-auth',
    version='0.0.2',
    description=('A collection of authentication extensions for Requests'),
    long_description=desc,
    url='https://github.com/jmvrbanac/requests-cloud-auth',
    author='John Vrbanac',
    author_email='john.vrbanac@linux.com',
    license='Apache v2',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    keywords='requests authentication cloud keystone extensions',
    packages=find_packages(exclude=['contrib', 'docs']),
    install_requires=['requests>=2.4.1'],
    package_data={},
    data_files=[],
    entry_points={
        'console_scripts': [],
    },
)
