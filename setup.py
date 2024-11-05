from setuptools import setup, find_packages

setup(
    packages=find_packages(
        include=["google_analytics_django", "google_analytics_django.*"]
    ),
    install_requires=[
        "django>=5.0,<6.0",
    ],
    extras_require={
        "dev": [
            "coverage>=7.6.3",
            "djlint>=1.35.2",
            "pre-commit>=4.0.1",
            "ruff>=0.6.9",
            "setuptools>=75.2.0",
        ]
    },
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
)
