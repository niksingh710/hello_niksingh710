from setuptools import setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='hello_niksingh710',
    version='0.0.1',
    description='Says Hello!',
    py_modules=['hello_niksingh710'],
    package_dir={'': 'src'},
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent"
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/niksingh710/hello_niksingh710",
    author="Nikhil Singh",
    author_email="nik.singh710@gmail.com"
)
