'''with open("weather.data.csv") as data_file:
    data = data_file.readlines()

import csv
with open("weather.data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    print(data)
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)'''

import pandas

data = pandas.read_csv('weather.data.csv')
#print(data["temp"])

#data_dict = data.to_dict()
#print(data_dict)

#temp_list = data['temp'].to_list()
#print(temp_list)
#print(len(temp_list))

#print(data['temp'].mean()) #average
#print(data['temp'].max()) #maximum

#get data in column
#print(data["condition"])
#print(data.condition)

#get data in row
#print(data[data.day == 'monday'])# or data[data['day']]
#print(data[data.temp == data.temp.max()])

#monday = data[data.day == 'monday']
#print(((monday.temp)*9/5)+32)

data_dict = {
    "students": ["amy","james","angela"],
    "scores": [76,56,65]
}
data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("new_data.csv")