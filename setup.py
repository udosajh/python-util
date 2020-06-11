import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='sqlite-util',  
     version='0.1',
     scripts=['sqlite-util'] ,
     author="Uday Dosajh",
     author_email="dosajhuday@gmail.com",
     description="sqlite utility",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/efficacious007/python-util",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "Operating System :: OS Independent"
     ],
 )