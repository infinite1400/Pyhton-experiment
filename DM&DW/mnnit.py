import requests
from bs4 import BeautifulSoup
# print(i)
x = requests.get(
    "https://www.netmeds.com/catalogsearch/result/paracetamol/all")
htmlContent = x.content
soup = BeautifulSoup(htmlContent, 'html.parser')
y = soup.find_all(class_=["clsgetname"])
# file = open("file.txt", "a", encoding='utf-8')
# file.write(title.text)
for i in y:
       for a in i.text.split("\n"):
            if (len(a) > 0):
                print(a+"\n")
            file.write("\n")
