# CCBCGE

The goal of this python package is to provide quick, easy acces to breast cancer gene expression data for analysis.

## Installation

To install this package, run the following command in your terminal:
```
pip install ccbcge
```

## Usage

There are four major functions that you can call.
1. `ChooseData()`
    a. This allows you see the list of data sets you can access and choose one to download.
    b. It returns two data sets: the gene expression data, then the meta data for that data set.
2. `ShowDataSets()`
    a. This shows the list of data sets you can access.
3. `importData(dataSet)`
    a. This takes as input the name of the data set you want to access.
    b. It returns the gene expression data of that name as a `pandas` data frame.
4. `importMeta(dataSet)`
    a. This takes as input the name of the data set you want to access.
    b. It returns the meta data for that data set as a `pandas` data frame.

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

The idea for this project came from a similar package from the Payne Lab at Brigham Young University, called `cptac`. To find out more about that package, visit the [CPTAC repository](https://github.com/PayneLab/cptac/)
