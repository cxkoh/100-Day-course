#errors
#file not found
#with open("a_file.txt") as file:
#   file.read()

#key error
#a_dict = {"key": "value"}
#value=a_dict["non_existant_key"]

#index error
#list=[0,1,2]
#number = list[3]

#type error
#text = "abc"
#print(text + 5)

'''exceptions
try:
    file = open("a_file.txt")
except:
    file = open("a_file.txt", "w")
    #or
    print("there was an error")'''

try:
    file = open("a_file.txt")
except FileNotFoundError:
    file = open("a_file.txt", "w")
    #or
    print("there was an error")
except KeyError:
    print("key does not exist")
except KeyError as error_message:
    print(f"key does not exist {error_message}")
else:#if try or except has no problem
    content = file.read()
    print(content)
finally:
    file.close()


#final key word
#raise own exceptions
finally:
raise TypeError("This is an error that i made up")




