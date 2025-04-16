import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fakemed",
    version="0.0.1",
    author="Brandon Payne",
    author_email="brandon.payne20@gmail.com",
    description="A package for generating fake medical data.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/brandonp/fakemed"
)