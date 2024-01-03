from bs4 import BeautifulSoup

with open("website.html", encoding="utf-8") as file:
    contents = file.read()


soup = BeautifulSoup(contents, "html.parser")
#print(soup.title)
#print(soup.prettify())
#print(soup.p)
all_anchor_tags = soup.find_all(name="a") #finding all ancor tag
print(all_anchor_tags)
for tag in all_anchor_tags:
    print(tag.get("href")) #find all href from all anchor tags

heading = soup.find(name="h1", id="name")
print(heading)

h3_heading = soup.find_all("h3")
print(h3_heading)

class_is_heading = soup.find_all(class_="heading")
print(class_is_heading)

name = soup.select_one(selector="#name")
print(name) #printing id of name

heading = soup.select(".heading")
print(heading)#printing all from heading class

