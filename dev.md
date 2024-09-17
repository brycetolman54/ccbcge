# Dev Docs

This is a markdown file containing instructions on how to update this project.

To see a list of tasks to accomplish, visit the [TODO page](TODO.md)

## Setup

To copy the repository to your local device, use the following:
```
git clone https://github.com/brycetolman54/ccbcge.git
```

Once done, run the .addAlias.sh file in the project folder using the following:
```
./.addAlias.sh
```

That will add an alias to your `.git/config` file that will allow for version tagging.


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

## Testing

If you want to test the package before uploading it, run the following (from the root of the project):
```
pip install -e .
```

This will allow you to download the package locally and will allow you to edit the package's source code and see the changes reflected in how it runs as you make them
