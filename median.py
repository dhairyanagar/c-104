import csv 

with open("heightweight.csv") as f:
    reader = csv.reader(f)
    data = list(reader)
    


data.pop(0)
new_data=[]
for i in range(len(data)):
    n_num =data[i][1]
    new_data.append(float(n_num))


    #getting mean
n=len(new_data)
new_data.sort()

#// floor division --- rounds off the result to nearest whole num
if n%2 == 0:
    median1=float(new_data[n//2])
    median2=float(new_data[n//2-1])
    median =(median1+median2)/2

else:
    median=new_data[n//2]
    print(n)

print(median)







