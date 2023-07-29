from skbuild import setup

setup(
    name="testing",
    description="a minimal example package (cpp version)",
    author="Dr Oliver Sheridan-Methven",
    # license="MIT",
    setuptools_git_versioning={"enabled": True},
    setup_requires=["setuptools-git-versioning<2"],
    packages=[
        "binding",
        "common",
        "media"
    ],
    package_dir={
        "binding": "src/binding",
        "common": "src/common",
        "media": "src/media"
    },
    python_requires=">=3.10",
)
