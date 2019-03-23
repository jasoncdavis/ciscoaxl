import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ciscoaxlsdk",
    version="1.0.0",
    author="Jeff Levensailor",
    author_email="jeff@levensailor.com",
    description="Cisco AXL library with with a goal of simple use.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/levensailor/ciscoaxlsdk",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)