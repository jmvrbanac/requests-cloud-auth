from setuptools import setup, find_packages

desc = ''
with open('README.rst') as f:
    desc = f.read()

setup(
    name='requests-cloud-auth',
    version='0.0.1',
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
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],

    keywords='requests authenication cloud keystone extensions',
    packages=find_packages(exclude=['contrib', 'docs', 'spec*']),
    install_requires=['requests>=2.4.1'],
    package_data={},
    data_files=[],
    entry_points={
        'console_scripts': [],
    },
)
