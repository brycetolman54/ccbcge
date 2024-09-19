# import data access functions
from .dataAccess import importData, importMeta, dataSets


# Function to display data sets and let the user choose which to use
#
# Returns: pandas data frames of the data and meta data
def ChooseData():

    # loop until a correct set is chosen
    while True:

        # display the data sets
        ShowDataSets()

        # read in the desired data set
        chosenSet = input("Choose a data set (0 for none): ")

        # Make sure the input is a number
        if not isinstance(chosenSet, int):
            print("Your input must be a number")
            continue

        # check the value given and set the appropriate values
        if chosenSet == 0:
            return
        elif chosenSet not in range(1, len(dataSets)):
            print("That is not an option")
            continue
        else:
            dataSet = dataSets[chosenSet - 1]
            break

    # return the values as calls to import the data
    return importData(dataSet), importMetaData(dataSet)


# Function to display data sets
def ShowDataSets():

    print("Data Sets:")
    for i in range(len(dataSets)):
        print(f"    {i + 1}) {dataSets[i]}")
