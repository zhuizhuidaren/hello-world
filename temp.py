import csv
import math

with open("data.csv","r") as df:
    data = csv.reader(df)
    count = 0
    sum = 0 
    for row in data:
        count += 1
        if count == 1:
            continue
        else:
            sum += math.pow(int(row[1])-float(row[3]),2)
    result = math.sqrt(sum/count)
    print(result)

# lalalalalalal  