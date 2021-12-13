
import csv 
from collections import Counter

with open("heightweight.csv") as f:
    reader = csv.reader(f)
    data = list(reader)
    


data.pop(0)
new_data=[]
for i in range(len(data)):
    n_num =data[i][1]
    new_data.append(float(n_num))


    #getting mode

data= Counter(new_data)

modedataforrange={
                    "50-60":0,
                    "60-70":0,
                    "70-80":0,
                }

for height, occurance in data.items():
    if 50<float(height)<60:
        modedataforrange["50-60"] += occurance

    elif 60<float(height)<70: 
        modedataforrange["60-70"] += occurance 

    elif 70<float(height)<80: 
        modedataforrange["70-80"] += occurance      


mode_range,mode_occurance=0,0
for range, occurance in modedataforrange.items():  
    if occurance>mode_occurance:
        mode_range,mode_occurance=[int(range.split("-")[0]),int(range.split("-")[1])] ,occurance

mode=float((mode_range[0]+mode_range[1])/2)
print(mode)











