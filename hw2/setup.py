import setuptools
with open("README.md", "r", encoding="utf-8") as fh: 
    long_description = fh.read()
setuptools.setup(
    name="filatov_latex_generator",
    version="1.1.0",
    author="Yuri Filatov",
    author_email="yura_filatov_2004@mail.ru",
    description="Lib for tables and pictures in latex",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/YuriiFilatov/pythonHW/hw2",
    packages=setuptools.find_packages("filatov_latex_generator"), 
    classifiers=[ "Programming Language :: Python :: 3", "License :: OSI Approved :: MIT License", "Operating System :: OS Independent", ],
    python_requires='>=3.7',)