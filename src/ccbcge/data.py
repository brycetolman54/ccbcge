import requests # type: ignore
import pandas as pd # type: ignore
from io import StringIO

def importData(url = "https://osf.io/download/ygfea"):
    data = requests.get(url)
    stringData = StringIO(data.text)
    df = pd.read_csv(stringData, sep='\t')
    return df

def printData(df):
    print(df)
