from skbuild import setup

setup(
    name="testing",
    version="1.2.3",
    description="a minimal example package (cpp version)",
    author="The scikit-build team",
    license="MIT",
    packages=["hello"],
    python_requires=">=3.7",
)