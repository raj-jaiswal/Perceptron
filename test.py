#  importing libraries
import Perceptron as ppt
import pandas as pd
from random import randint
import mysql.connector as msq

#  Connecting to the database
con=msq.connect(
  host="localhost",
  user="user",
  passwd="",
  database="data"
)
cursor=con.cursor()

#  Accessing data from database
data=pd.read_sql('SELECT * FROM data',con)
#  Find the minimum and maximum values from the data
mins=data.min()
maxs=data.max()

#  Normalizing the data
temp=((data-mins)/(maxs-mins)).fillna(0)
data.iloc[:,:6]=temp.iloc[:,:6]

#  Creating perceptron
perceptron=ppt.Perceptron(data.columns.size-1,0.1)
print(data)

#  Calculate the accuracy of Perceptron
def score():
    summ=0
    for i in range(data.index.size):
        summ+=(data.iloc[i,6]-perceptron.predict(list(data.iloc[i,:6].values)))**2
    return summ**0.5/data.index.size

print()
print('Initial Score:',score())
#  Train the perceptron with the data
for i in range(1000):
    item=data.iloc[randint(0,data.index.size-1),:]
    perceptron.train(list(item[:6].values),item[6])
print('Final Score:',score())

try:
    #input data from user to predict result
    print('\n')
    print('Enter details of the phone-')
    RAM=int(input('RAM: '))
    storage=int(input('Storage: '))
    camera=int(input('camera: '))
    battery=int(input('battery: '))
    CPUCores=int(input('CPUCores: '))
    refreshRate=int(input('refreshRate: '))
    
    #Normalizing the Data given by user
    RAM=(RAM-mins[0])/(maxs[0]-mins[0])
    storage=(storage-mins[1])/(maxs[1]-mins[1])
    camera=(camera-mins[2])/(maxs[2]-mins[2])
    battery=(battery-mins[3])/(maxs[3]-mins[3])
    CPUCores=(CPUCores-mins[4])/(maxs[4]-mins[4])
    refreshRate=(refreshRate-mins[5])/(maxs[5]-mins[5])

    #Predict the result from data given by user
    result=perceptron.predict([RAM,storage,camera,battery,CPUCores,refreshRate])
    print()
    if result>0:
        print('Its a flagship phone.')
    else:
        print('Its is a budget phone.')
    
except ValueError:
    pass

except KeyboardInterrupt:
    pass
