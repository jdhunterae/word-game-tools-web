from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="word-game-tools-web",
    version="0.1.0",
    author="Andrew Pomerleau",
    author_email="arpomerleau@gmail.com",
    description="A collection of tools for solving word games",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jdhunterae/word-game-tools-web",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Games/Entertainment :: Puzzle Games",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=[
        "click>=8.0.0",
        "python-dotenv>=0.19.0",
        "Flask>=2.0.0",
        "Flask-WTF>=1.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=3.0.0",
            "black>=22.0.0",
            "flake8>=4.0.0",
            "isort>=5.0.0",
            "mypy>=0.950",
            "Sphinx>=4.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "bee-helper=wordgames.cli.bee_helper:main",
            # Add more CLI scripts here as they're developed
        ],
    },
    package_data={
        "wordgames": ["data/*.txt"],  # Include dictionary files
    },
    include_package_data=True,
)
