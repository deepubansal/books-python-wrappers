import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="zohobooks-python", # Replace with your own username
    version="0.0.1",
    author="deepubansal",
    author_email="deepu.bansal@gmail.com",
    description="Zoho Books Python wrapper package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/deepubansal/books-python-wrappers",
    packages=setuptools.find_packages(),
    classifiers=[
    ]
)