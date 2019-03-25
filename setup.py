from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="ciscoaxl",
    version="0.0.1",
    author="Jeff Levensailor",
    author_email="jeff@levensailor.com",
    description="Cisco CUCM AXL Library. Simple to use.",
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/levensailor/ciscoaxlsdk",
    keywords=['Cisco', 'Call Manager', 'CUCM', 'AXL', 'VoIP'],
    packages=['ciscoaxl'],
    include_package_data=True,
    install_requires = [
    'suds-jurko==0.6',
    'urllib3==1.23'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)