# This Module is used to actually access the data sets and bring them down
# from the web.
#
# Below are the possible data sets that we have added, the URLs for the metadata 
# and the URLs for the actual data
#
# Users can call these functions directly (f they know the data set name)
# or do so through the functions of the __init__.py functions that let 
# them see and choose the data sets they want to bring down


import requests # type: ignore
import pandas as pd # type: ignore
import gzip as gz
from io import StringIO, BytesIO


# Value containing the names of accessible data sets
dataSets = [
    "ETABM",
    "GSE11001",
    "GSE11121",
]


# Value containing the urls for the gene expression data
dataURLs = [
    "https://osf.io/download/k52ux",
    "https://osf.io/download/tfud9",
    "https://osf.io/download/fp7xr",
]


# Value containing the urls for the meta data
metaDataURLs = [
    "https://osf.io/download/ygfea",
    "https://osf.io/download/j6bfc",
    "https://osf.io/download/kywrv",
]


# Function to import the metadata
#
# input: the name of a data set in string form
#
# returns: a pandas data frame
def importMeta(dataSet):

    # check that the type of the input is a string
    if not isinstance(dataSet, str):
        print("Error: Function takes as input a string")
        return None

    # check if the dataSet is one in the list
    if dataSet in dataSets:
        # grab the index of the dataSet
        index = dataSets.index(dataSet)
    else:
        print("Error: No data set of that name")
        return None

    # grab the meta data url
    url = metaDataURLs[index]

    # access the data and place it in a data frame
    data = requests.get(url)
    stringData = StringIO(data.text)
    df = pd.read_csv(stringData, sep = '\t')
    return df


# Function to import the gene expression data
#
# input: the name of a data set in string form
#
# returns: a pandas data frame
def importData(dataSet):

    # check that the type of the input is a string
    if not isinstance(dataSet, str):
        print("Error: Function takes as input a string")
        return None

    # check if the dataSet is one in the list
    if dataSet in dataSets:
        # grab the index of the dataSet
        index = dataSets.index(dataSet)
    else:
        print("Error: No data set of that name")
        return None

    # grab the gene expression data url
    url = dataURLs[index]

    # access the data and place it in a data frame
    zipData = requests.get(url)
    bytesData = gz.decompress(zipData.content)
    data = BytesIO(bytesData)
    df = pd.read_csv(data, sep = '\t')
    return df
