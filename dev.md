# Dev Docs

This is a markdown file containing instructions on how to update this project.

To see a list of tasks to accomplish, visit the [TODO page](TODO.md)

## Setup

In order to update the package in PyPI, you need to be added as a collaborator on that site.
If you do not already have an account on PyPI, go [create one](https://pypi.org/account/register/).
After that, contact Dr. Piccolo and provide him your username so he can add you to the project.

To copy the package repository to your local device, use the following:
```
git clone https://github.com/brycetolman54/ccbcge.git
```

Once done, run the .addAlias.sh file in the project folder using the following:
```
./.addAlias.sh
```

This will add an alias to your `.git/config` file that will allow for version tagging.
You must update the version every time you try to update the package in PyPI.


You will need twine to update the package on PyPI. Install it using the following:
```
pip install twine
```

## Tagging New Versions

To tag a new version (and have it update in your `pyproject.toml` and `version.py` files), run the following:
```
git tv <version> "<mesage>"
```

An example of this would be:
```
git tv v0.1.4 "Added new data set"
```

After you tag a new version, for that version to reflect on GitHub, you have to go to the package site and create a new release 
in the side bar of the home page.
1. Click on "Releases"
2. Click on "Draft a new release"
3. Choose the Tag to use
4. Give the release a name (the version number in format "vx.x.x" typically)
5. Write a message about what the release updates from the past release
6. Make sure the "Set as the latest release" checkbox is marked
7. Click "Publish release"

## Updating the Package on PyPI

To update the package on PyPI, do the following:

- Build the project (from the root of the project)
```
python -m build
```

- Upload with twine (from the root of the project)
```
twine upload dist/*
```

Remove the `dist/` directory
```
rm -rf dist/*
```

## Adding Data

There is an array called `dataSets` which contains the names of the different data sets we have on [OSF](https://osf.io/eky3p/?view_only=).
There is an array called `dataURLs` which contains the URLs of each gene expression data set in the form: `https://osf.io/download/{dataSetId}`.
There is an array called `metaDataURLs` which contains the URLs of the meta data for each data set in the form: `https://osf.io/download/{metaDataSetId}`.
In order to add new data, you only need to add the name of the data set to the first array and the URLs for the gene expression data set and metadata set
to the second and third data arrays.


## Testing

If you want to test the package before uploading it, run the following (from the root of the project):
```
pip install -e .
```

This will allow you to download the package locally and will allow you to edit the package's source code and see the changes reflected in how it runs as you make them
