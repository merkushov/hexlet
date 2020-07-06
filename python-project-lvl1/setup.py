import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="merkushov-brain-games",
    version="0.1.7",
    author="Victor Merkushov",
    author_email="merkushov.victor@gmail.com",
    description="A small test package",
    long_description="A small test package",
    long_description_content_type="text/markdown",
    url="https://github.com/merkushov/hexlet.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3"
    ],
    python_requires='>=3.6'
)
