# CCBCGE

The goal of this python package is to provide quick, easy access to breast cancer gene expression data from OSF for analysis.

You can view this python package on its [PyPI Site](https://pypi.org/project/ccbcge/)

## Installation

Since this is a python package, you must have python installed on your computer. This package calls for Python 3.8 or greater.

To install this package, run the following command in your terminal:
```
pip install ccbcge
```

## Usage

There are four major functions that you can call.
1. `ChooseData()`
    - This allows you see the list of data sets you can access and choose one to download.
    - It returns two data sets: the gene expression data, then the meta data for that data set.
4. `ShowDataSets()`
    - This shows the list of data sets you can access.
5. `importData(dataSet)`
    - This takes as input the name of the data set you want to access.
    - It returns the gene expression data of that name as a `pandas` data frame.
6. `importMeta(dataSet)`
    - This takes as input the name of the data set you want to access.
    - It returns the meta data for that data set as a `pandas` data frame.

The idea behind these functions is that you can access the data frame easily by name if you 
already know which data set you want to access.

For those who do not know which data sets they want to access, however, they have the option
of seeing the data sets and choosing from them the one they want to work with.

If you want to use all of the data, you could write a simple for loop as follows:
```
for dataSet in dataSets:
    geneData = importData(dataSet)
    metaData = importMeta(dataSet)

    # analyze the data here
```


## Dependencies

This package requires use of the following packages:
- `request`
- `pandas`

If you do not have them installed already, they will be installed for you.

## Development

Help for how to update this package is found in a [Developers File](dev.md)

## License

This project is licensed under the Apache 2.0 License - see the [LICENSE](LICENSE) file for more information.

## Acknowledgements

The idea for this project came from a similar package from the Payne Lab at Brigham Young University, called `cptac`.
To find out more about that package, visit the [CPTAC Github repository](https://github.com/PayneLab/cptac/)
or the [CPTAC PyPI package](https://pypi.org/project/cptac/).
