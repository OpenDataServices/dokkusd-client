import setuptools

setuptools.setup(
    name="DokkuSD",
    version="0.4.0",
    description="DokkuSD",
    long_description="DokkuSD",
    url="https://github.com/OpenDataServices/dokkusd-client",
    project_urls={
        "Documentation": "https://dokkusd-client.readthedocs.io/en/latest/",
        "Issues": "https://github.com/OpenDataServices/dokkusd-client/issues",
        "Source": "https://github.com/OpenDataServices/dokkusd-client",
    },
    author="Open Data Services",
    author_email="code@opendataservices.coop",
    license="MIT",
    packages=setuptools.find_packages(exclude=["test"]),
    classifiers=[],
    install_requires=[],
    extras_require={
        "Dev": [
            "sphinx",
            "black==22.8.0",
            "isort==5.10.1",
            "flake8==5.0.4",
            "mypy==0.981",
            "pytest",
        ]
    },
    python_requires=">=3.7",
)
