import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    include_package_data=True,
    name="hyperpub", # Replace with your own username
    version="0.0.1",
    author="Peder Landsverk",
    author_email="pglandsverk@gmail.com",
    description="LitProg. publishables with CSS / HTML",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Peder2911/hyperpub",
    packages=setuptools.find_packages(),
    scripts= ["bin/hyperpub"],

    package_data = {
        "templates":["*"],
        "hyperpub":["html/*","css/*","templates/*"]
    },

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    install_requires=[
        "Jinja2==2.11.2",
        "pandas==1.0.4",
        "fire==0.3.1"
    ]
)
