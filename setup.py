from setuptools import setup, find_packages


setup(
    name="LngDetectoR",
    version="2025.5.81751",
    author="Eugene Evstafev",
    author_email="chigwel@gmail.com",
    description="A tool to detect programming languages in a directory.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/chigwell/langdetector",
    packages=find_packages(),
    install_requires=[
        "prettytable",
        "python-magic",
    ],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "lngdetector = lngdetector.detect:main",
        ],
    },
)
