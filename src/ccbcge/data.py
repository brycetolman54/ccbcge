import requests # type: ignore
import pandas as pd # type: ignore
import gzip as gz
from io import StringIO, BytesIO

def importMeta(url = "https://osf.io/download/ygfea"):
    data = requests.get(url)
    stringData = StringIO(data.text)
    df = pd.read_csv(stringData, sep = '\t')
    return df

def printMeta(df):
    print(df)

def importData(url = "https://osf.io/download/k52ux"):
    zipData = requests.get(url)
    bytesData = gz.decompress(zipData.content)
    data = BytesIO(bytesData)
    df = pd.read_csv(data, sep = '\t')
    return df

def printData(df):
    print(df)
