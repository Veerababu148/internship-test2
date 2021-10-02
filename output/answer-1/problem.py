# first table u have to read the file 

import pandas
v=pandas.read_csv("internship-test2/input/question-1/main.csv")
for year in v:
  if(year%10==0):
    print(year)

for Violent in v:
  total+=Violent
  print(total)
for Property in v:
  total+=Property
  print(total)
for Murder in v:
  total+=Murder
  print(total)
for Forcible_Rape in v:
  total+=Forcible_Rape
  print(total)
for Robbery in v:
  total+=Robbery
  print(total)
for Aggravated_assault in v:
  total+=Aggravated_assault
  print(total)
for Burglary in v:
  total+=Burglary
  print(total)
for Larceny_Theft in v:
  total+=	Larceny_Theft
  print(total)
for Vehicle_Theft in v:
  total+=	Vehicle_Theft
  print(total)
 
  

  
