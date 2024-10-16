from setuptools import setup, find_packages

setup(
    name="google-analytics-django",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,  
    install_requires=[
        "Django>=5.1.2",
    ],
    classifiers=[
        "Framework :: Django",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',  
    author="Adivhaho Mavhungu",
    author_email="adivhahomavhungu@outlook.com",
    description="A Django package to integrate Google Analytics.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/mavhungutrezzy/google_analytics_django",  
    project_urls={
        "Bug Tracker": "https://github.com/mavhungutrezzy/google_analytics_django/issues", 
    },
)
