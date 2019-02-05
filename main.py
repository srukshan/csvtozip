path=""
hasCsv = -1
while((path=="")|(hasCsv==-1)):
    path = input("Enter the csv Path : ")
    path = str.strip(path)
    hasCsv = path.find(".csv")

des=""
while(des==""):
    des = input("Enter the destination Path : ")
    des = str.strip(des)

import csv

rootdir = "temp/"

results = []
with open(path) as csvfile:
    reader = csv.reader(csvfile) # change contents to floats
    init = 0
    for row in reader: # each row is a list
        if init==0:
            init+=1
            continue
        results.append(row)

from downloader import download, getDestination, downloader
import os

if not(os.path.exists(rootdir)):
    os.makedirs(rootdir)

from multiprocessing import Pool
from itertools import product

pool = Pool(20)

down = downloader(rootdir)

pool.map(down.downloadSet, results)
pool.join()
pool.close()

print("Download Complete")

from shutil import make_archive

archiveName = path.rsplit('/',1)[1]
archiveName = archiveName.split('.')[0]
archiveName = des+archiveName

make_archive(archiveName, 'zip', rootdir)
print("Compression Finished")