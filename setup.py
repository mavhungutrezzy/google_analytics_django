from setuptools import setup, find_packages

setup(
    name="google-analytics-django",
    version="0.1.0",
    description="A Django package to integrate Google Analytics.",
    packages=find_packages(
        include=["google_analytics_django", "google_analytics_django.*"]
    ),
    install_requires=[
        "coverage>=7.6.3",
        "django>=5.1.2",
        "djlint>=1.35.2",
        "pre-commit>=4.0.1",
        "ruff>=0.6.9",
        "setuptools>=75.2.0",
    ],
    python_requires=">=3.12",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
)
