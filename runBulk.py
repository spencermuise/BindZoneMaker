#!/bin/python3

import os
import sys
from pathlib import Path

if Path("zones.txt").is_file() == False:
    print('zones.txt is missing, it should be in the same folder as this script')
    exit()

if len(sys.argv) > 1:
    argv = sys.argv[1]
else: argv = None

if argv == "-h":
    print("put the list of zones in 'zones.txt', place the .json files in a folder called 'input'. bind files will be created in the 'output' folder")
    exit()

zoneList = open('zones.txt')

with open('zones.txt') as f:
    zoneCount = sum(1 for _ in f)

if zoneCount > 0:
    Path("output").mkdir(parents=True, exist_ok=True)
else:
    exit()

processedCount = 0

for zoneLine in zoneList:
    zone = zoneLine.rstrip('\n')
    zoneInput = Path('input/{zoneName}.json'.format(zoneName = zone))
    zoneOutput = Path('output/{zoneName}'.format(zoneName = zone))
    if zoneOutput.is_file() and argv != "-f":
        print('output file for {zoneName} already exists. pass -f to overwrite'.format(zoneName = zone))
    else:
        if zoneInput.is_file():
            os.system('python bindZoneMaker.py -z input/{zoneName}.json > output/{zoneName}'.format(zoneName = zone))
            print('{zoneName} processed'.format(zoneName = zone))
            processedCount +=1
        else:
            print('{zoneName} not found in input folder'.format(zoneName = zone))

print('{processedZones}/{totalZones} zones processed successfully'.format(processedZones = processedCount, totalZones = zoneCount))