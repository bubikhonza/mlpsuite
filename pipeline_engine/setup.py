from setuptools import setup, find_packages

setup(
    name="pipeline_engine",
    author="bubikhonza@gmail.com",
    version="0.1",
    packages=["pipeline_engine"],
    package_dir={'pipeline_engine': 'src/pipeline_engine'},
    requires=["pyyaml"]
)
