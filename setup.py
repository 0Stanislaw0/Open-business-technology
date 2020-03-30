import setuptools

setuptools.setup(
    name="m3", #
    version="0.1.1",
    author="Stanislav",
    author_email="stas.yyyy20@gmail.com",
    description="s",
    long_description="long_description",
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    install_requires=['django==1.11','m3-objectpack==2.2.25'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
