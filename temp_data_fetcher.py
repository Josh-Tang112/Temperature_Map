import requests
from io import BytesIO
import gzip

baseURL = "https://www.ncei.noaa.gov/pub/data/ghcn/daily/by_station/"
filename = "ACW00011604.csv.gz"
outFilePath = "ACW00011604.csv"

r = requests.get(baseURL + filename)
compressedFile = BytesIO()
compressedFile.write(r.content)
compressedFile.seek(0)

decompressedFile = gzip.GzipFile(fileobj=compressedFile, mode='rb')

# with open(outFilePath, 'wb') as outfile:
#     outfile.write(decompressedFile.read())

# check https://www.ncei.noaa.gov/pub/data/ghcn/daily/readme.txt for details
print(decompressedFile.read(50).decode("utf-8"))
