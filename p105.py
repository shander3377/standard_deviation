import csv
import math
with open('C:/Users/pankaj/Desktop/agrim/coding/c97/std_deviation/data.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)
data = file_data[0]
def mean(data):

 num = len(data)
 total = 0
 for numbers in data:
     total+=int(numbers)
 mean = total/num
 return mean
#step2
sqrList = []
for numbers in data:
  
    
    subtracted = int(numbers)-mean(data)
    a=subtracted**2
    sqrList.append(a)

sum = 0
for i in sqrList:
      sum = sum+i
result = sum/(len(data)-1)
    
standard_Deviation = math.sqrt(result)
print(standard_Deviation)