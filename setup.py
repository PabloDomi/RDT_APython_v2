# setup.py (for backward compatibility)
from setuptools import setup, find_packages

setup(
    name="rdt-api-generator",
    version="2.0.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "click>=8.1.7",
        "jinja2>=3.1.2",
        "pydantic>=2.5.0",
        "pydantic-settings>=2.1.0",
        "rich>=13.7.0",
        "inquirerpy>=0.3.4",
        "colorama>=0.4.6",
    ],
    entry_points={
        'console_scripts': [
            'rdt=rdt.cli.commands:cli',
        ],
    },
    author="Your Name",
    author_email="your.email@example.com",
    description="Professional API project generator for Python",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/rdt",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.11",
)