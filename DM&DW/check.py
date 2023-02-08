import requests
from bs4 import BeautifulSoup
file = open("output.txt", "w", encoding='utf-8')
file.close()
element1 = []
element1.append("http://ce.nits.ac.in/faculty/")
element1.append("http://me.nits.ac.in/faculty/")
element1.append("http://eie.nits.ac.in/faculty/")
element1.append("http://cs.nits.ac.in/faculty/")
element1.append("http://ec.nits.ac.in/faculty/")
element1.append("http://eed.nits.ac.in/faculty/")




for i in element1:
    print(i)
    x = requests.get(i)
    htmlContent = x.content
    soup = BeautifulSoup(htmlContent, 'html.parser')
    y = soup.find_all( 'div',class_=["panel-group","tab-content"])
    file = open("file.txt", "a", encoding='utf-8')
    # i=y.find_all('a')
    for i in y:
        # print(i.text)
        for j in y:
            for a in j.text.split("\n"):
                if (len(a) > 5):
                 file.write(a+"\n")
            file.write("\n")
element1.clear()