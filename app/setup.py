from setuptools import setup, find_packages

setup(
    name="pipeliner",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'pyspark',
        'pyyaml',
    ],
    packages = find_packages(),  # include all packages under src
)
