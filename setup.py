from setuptools import find_packages, setup

with open('README.md', 'r') as f:
    long_description=f.read()

setup(
    name="cli-template",
    version="0.0.0",
    author="ElDiabloRojo",
    author_email="holdens.uk@googlemail.com",
    description="Template for creating python command line tools.",
    long_description=long_description,
    long_description_content_type="test/markdown",
    url="https://github.com/ElDiabloRojo/py-cli-template",
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=['boto3'],
    entry_points={
        'console_scripts:' [
            's3_client=s3_client.cli:main'
        ],

    }
)