# Advanced

[TOC]

## Updating the remote documentation. 

To update the documentation hosted remotely (e.g. on GitHub Pages), 
then on `master` we need to redeploy the documents after 
the most relevant commit by calling:
```bash
mkdocs gh-deploy --clean
```

!!! note "TODO: Git hooks"
    I should automate this by turning this into a git hook
    or a github action. 
