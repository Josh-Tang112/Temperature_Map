import requests
from io import BytesIO, StringIO
import gzip
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
import math

# check https://www.ncei.noaa.gov/pub/data/ghcn/daily/readme.txt for details about csv format

def get_station_name(lat,lng):
    f = open("temperature/data/stations.txt")
    lst = f.readlines()
    min_name = ''
    min_distance = -1
    for line in lst:
        token = re.split('[ ]+',line)
        distance = math.sqrt((float(token[1]) - lat)**2 + (float(token[2]) - lng)**2)
        if min_distance < 0:
            min_distance = distance
        elif min_distance > distance:
            min_distance = distance
            min_name = token[0]
    return min_name

def drop_out_NULL(df):
    # value of -9999 indicates missing
    return df.drop(df.loc[df['VALUE1']==-9999].index.values.astype(int))
def drop_out_non_temperature(df):
    # I'm only interested in temperature data
    return df.loc[(df['ELEMENT']=='TMIN') | (df['ELEMENT']=='TMAX')]

def get_fig(station_name):
    baseURL = "https://www.ncei.noaa.gov/pub/data/ghcn/daily/by_station/"
    filename = f"{station_name}.csv.gz"
    outFilePath = f"{station_name}.csv"
    print(station_name)

    r = requests.get(baseURL + filename)
    compressedFile = BytesIO()
    compressedFile.write(r.content)
    compressedFile.seek(0)

    decompressedFile = gzip.GzipFile(fileobj=compressedFile, mode='rb')

    # with open(outFilePath, 'wb') as outfile:
    #     outfile.write(decompressedFile.read())

    buffer = StringIO()
    buffer.write("ID,DATE,ELEMENT,VALUE1,MFLAG,QFLAG,SFLAG,VALUE2\n")
    buffer.write(decompressedFile.read().decode("utf-8"))
    buffer.seek(0)
    df = pd.read_csv(buffer)

    flag = [0,0]
    if len(df.loc[(df['ELEMENT']=='TMAX')]) > 0:
        flag[0] = 1
    if len(df.loc[(df['ELEMENT']=='TMIN')]) > 0:
        flag[1] = 1
    if flag[0] == 0 and flag[1] == 0:
        return 0

    df = drop_out_non_temperature(df)
    df = drop_out_NULL(df)
    df['VALUE1'] = df['VALUE1'].map(lambda x : x / 10) # values of temperature arein tenths of celsius
    df['DATE'] = df['DATE'].map(lambda x : int(x / 10000)) # I'm only interested in yearly average
    df = df[['DATE','ELEMENT','VALUE1']]
    df = df.groupby(['ELEMENT','DATE']).mean()

    # creating the graph
    fig, ax = plt.subplots(figsize=(10,5))
    if flag[0] == 1:
        plt.plot(df.loc['TMAX'].index,np.reshape(df.loc['TMAX'].values,
            len(df.loc['TMAX'].values)),label="Yearly Average Max Temperature")
    if flag[1] == 1:
        plt.plot(df.loc['TMIN'].index,np.reshape(df.loc['TMIN'].values,
            len(df.loc['TMIN'].values)),label="Yearly Average Min Temperature")
    plt.ylabel("Temperature in Celsius")
    plt.xlabel("Year")
    plt.legend()
    plt.savefig("temperature/lol.jpg")

    return 1
