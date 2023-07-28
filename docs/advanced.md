# Advanced

## Updating the remote documentation. 

To update the documentation hosted remotely (e.g. on GitHub Pages), 
then on `master` we need to redeploy the documents after 
the most relevant commit by calling:
```bash
mkdocs gh-deploy --clean
```

Additionally, to tage the appropriate version, run:
```bash
mike deploy --push --update-aliases <TAG> latest
```

