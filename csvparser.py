import csv
import collections

typePoints = collections.Counter()

def data_points(data):
    count = 0 
    for line in data:
        count += 1 #counter
    return count

def count_types(rows):
    pointsType = []
    for row in rows:
        if len(row) >= 4:
            typePoints[row[3]] += 1

    for key in sorted(typePoints):
        pointsType.append(f"{key}: {typePoints[key]}")
    
    return (', '.join(pointsType))

def maintenance(rows):
    needMaint = []
    for row in rows:
        if int(row[5]) < 3:
            needMaint.append(row[0])
    return(', '.join(needMaint))

def inspection(rows):
    lastInspect = []
    for row in rows:
        if row[6] < "2024-01-01":
            lastInspect.append(row[0])
    return(', '.join(lastInspect))

def minmaxBounds(row):
    Latitude, Longitude = [], []
    for row in rows:
        Latitude.append(float(row[1]))
        Longitude.append(float(row[2]))
    minLat = min(Latitude)
    maxLat = max(Latitude)
    minLong = min(Longitude)
    maxLong = max(Longitude)
    return minLat, maxLat, minLong, maxLong

#read the CSV file
with open('gis_data.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    data = list(csv_reader)

    header = data[0] 
    rows = data[1:] #all other data, no header

    count = data_points(rows)
    types = count_types(rows)
    maint = maintenance(rows)
    inspect = inspection(rows)
    minValLat, maxValLat, minValLong, maxValLong  = minmaxBounds(rows)


    file = open('ExpectedOutput.txt', 'w')

    file.write(f"Total number of points: {count} \n")
    file.write(f"Count of points by type: {types} \n")
    file.write(f"Points requiring maintenance: {maint} \n")
    file.write(f"Points not inspected in the last year include: {inspect} \n")
    file.write(f"The Min Lat value is: {minValLat}, | Max Lat: {"%.4f" % maxValLat} | Min Long: {minValLong} | Max Long: {"%.4f" % maxValLong}")

    file.close()