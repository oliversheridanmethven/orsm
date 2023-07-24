from skbuild import setup

setup(
    name="testing",
    version="1.2.3",
    description="a minimal example package (cpp version)",
    author="The scikit-build team",
    license="MIT",
    packages=["hello", "foo"],
    # package_dir={"bar": "foo/bar"},
    # packages=["hello", "hello_world_c"],
    # package_dir={"hello_world_c": "src.binding"},
    python_requires=">=3.7",
)