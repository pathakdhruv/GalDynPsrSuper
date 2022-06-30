import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="GalDynPsrSuper",
    version="v0.0.4",
    author="Dhruv Pathak",
    author_email="pathakdhruv9786@gmail.com",
    license='New BSD',
    description="A package for estimating contribution of dynamical terms in the first and second derivatives of frequencies (both spin and orbital) of pulsars.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pathakdhruv/GalDynPsrSuper",
    include_package_data=True,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
)
