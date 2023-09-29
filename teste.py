import datetime
current_date = datetime.datetime.now()
x = str(current_date)
#print(x[0:10])
born = '27/09/2009'
y= int(born[6:10])
m = int(born[4:5])
d= int(born[0:2])
#print(type(type (x[0:4])))
year = int(x[0:4])- y
month= int(x[5:7])- m
day= int(x[8:10])-d

print(year, month, day)
if (year>18): print('é de maior')
elif (year<17):  print('é de menor')
elif (month>=0 and day>=0):  print('é de maior ')
else: print('é de menor')


