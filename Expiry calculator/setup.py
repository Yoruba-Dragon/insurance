from setuptools import setup, find_packages

setup(
    name="expiry_calculator",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'python-dateutil',  # This is for relativedelta
    ],
    description="A package to calculate the expiry date of insurance policies",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    author="Pelumi",
    author_email="your_email@example.com",
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)