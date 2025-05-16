import csv
import collections

typePoints = collections.Counter()

#creation of functions
#Returns the total amount of data points found in the CSV file
def data_points(data):
    count = 0 
    for line in data:
        count += 1 #counter
    return count

#Returns the type and their quantity
def count_types(rows):
    pointsType = []
    for row in rows:
        if len(row) >= 4:
            typePoints[row[3]] += 1

    for key in sorted(typePoints):
        pointsType.append(f"{key}: {typePoints[key]}")
    
    return (', '.join(pointsType))

#Returns the points that are requiring maintenance
def maintenance(rows):
    needMaint = []
    for row in rows:
        if int(row[5]) < 3:
            needMaint.append(row[0])
    return(', '.join(needMaint))

#Returns the points not inspected in the last year
def inspection(rows):
    lastInspect = []
    for row in rows:
        if row[6] < "2024-01-01":
            lastInspect.append(row[0])
    return(', '.join(lastInspect))

#Returns Min/ Max Latitude and Longitude values
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

#Returns first and last install by date
def installDate(row):
    totalDate = []
    for row in rows:
        totalDate.append(row[4])
    return min(totalDate), max(totalDate)

#read the CSV file
with open('gis_data.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    data = list(csv_reader)

    header = data[0] 
    rows = data[1:] #all other data, no header

    #Calling functions
    count = data_points(rows)
    types = count_types(rows)
    maint = maintenance(rows)
    inspect = inspection(rows)
    minValLat, maxValLat, minValLong, maxValLong  = minmaxBounds(rows)
    fInstall, lInstall = installDate(rows)

    #Prompt user to make a choice
    print("Pick your report (1-7)")
    print("1. Total number of points in the dataset")
    print("2. Count of points by type")
    print("3. Point requiring maintenance (Condition rating < 3)")
    print("4. Points not inspected in the last year (2024)")
    print("5. Geographical bounds of the dataset (min/max Latitude and Longitude)")
    print("6. First and last install dates")
    print("7. Full report")

    choice = input("Pick your report: ")

    #Writes to a txt file per your choice
    if choice == '1':
        file = open('ExpectedOutput.txt', 'w')
        file.write(f"Total number of points: {count}")
        file.close()
    elif choice == '2':
        file = open('ExpectedOutput.txt', 'w')
        file.write(f"Count of points by type: {types}")
        file.close()
    elif choice == '3':
        file = open('ExpectedOutput.txt', 'w')
        file.write(f"Points requiring maintenance: {maint}")
        file.close()
    elif choice == '4':
        file = open('ExpectedOutput.txt', 'w')
        file.write(f"Points not inspected in the last year include: {inspect}")
        file.close()
    elif choice == '5':
        file = open('ExpectedOutput.txt', 'w')
        file.write(f"The Min Lat value is: {minValLat}, | Max Lat: {"%.4f" % maxValLat} | Min Long: {minValLong} | Max Long: {"%.4f" % maxValLong}")
        file.close()
    elif choice == '6':
        file = open('ExpectedOutput.txt', 'w')
        file.write(f"First install date: {fInstall} | Last install date: {lInstall}")
        file.close()
    elif choice == '7':
        file = open('ExpectedOutput.txt', 'w')
        file.write(f"Total number of points: {count} \n")
        file.write(f"Count of points by type: {types} \n")
        file.write(f"Points requiring maintenance: {maint} \n")
        file.write(f"Points not inspected in the last year include: {inspect} \n")
        file.write(f"The Min Lat value is: {minValLat}, | Max Lat: {"%.4f" % maxValLat} | Min Long: {minValLong} | Max Long: {"%.4f" % maxValLong} \n")
        file.write(f"First install date: {fInstall} | Last install date: {lInstall}")
        file.close()
    else:
        print("Invalid. Try again.")
        