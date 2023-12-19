number = [ 1,2,3]
new_list = []
import random
 #for n in number:
  #   add_1 = n + 1
   #  new_list.append()
#new_list = [new_item for item in list]
#new_list = [n+1 for n in number]
#new_dict = {new_key:new_value for item in list}
#new_dict = {new_key:new_value for (key,value) in dict.items()}

names = ['alex','beth','caro','dave']
student_score = {n:random.randint(0,100) for n in names}
print(student_score)
passed_students = {n:score for (n,score) in student_score.items() if score >= 60}

student_dict = {
    "student": ["angela", "james", "lily"]
    "score": [56, 76,98]
}

import pandas

student_data_frame = pandas.DataFrame
(student_dict)
#print(student_data_frame)

#Loop through a data frame
for (key,value) in student_data_frame.items():
    print(key) #output(student , score)
    print(value) #output(key and values)

#Loop through rows of a date frame
for (index, row) in student_data_frame.iterrows():
    print(index)
    print(row)
    print(row.student) #to give student column

#finding out student score
for (index, row) in student_data_frame.iterrows():
    if row.student == "angela":
        print(row.score)
