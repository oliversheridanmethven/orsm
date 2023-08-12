# Advanced

## Updating the git versions and releases

To list the git version tags: 
```bash
git tag -l
```

To add a tag use:
```bash
git tag -a <vX.Y.Z> -m "<SOME BRIEF MESSAGE>"
```

To set a release with a tag:
```bash
gh release create $(git describe --tags --abbrev=0)
```

## Updating the remote documentation. 

To update the documentation hosted remotely (e.g. on GitHub Pages), 
then on `master` we need to redeploy the documents after 
the most relevant commit by calling:
```bash
mkdocs gh-deploy --clean
```

