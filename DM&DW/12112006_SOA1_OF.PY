import requests
from bs4 import BeautifulSoup
url = "https://nitkkr.ac.in/?page_id=791"
r = requests.get(url)
htmlContent = r.content

soup = BeautifulSoup(htmlContent, 'html.parser')

title = soup.title

element1 = soup.find_all(class_=["hd", "left-sec"])

file = open("output.txt", "w")
file.write(title.text)
for element in element1:
    for a in element.text.split("\n"):
        if (len(a) > 0):
            # print(a, "\n------------------")
            file.write(a+"\n")
    file.write("\n")

file.close()

url = "http://www.mnnit.ac.in/index.php/department/engineering/csed/csedfp"

r = requests.get(url)
htmlContent = r.content

soup = BeautifulSoup(htmlContent, 'html.parser')

title = soup.title

element1 = soup.find_all(id="fav-container")

file = open("output.txt", "a",encoding='utf-8')
file.write(title.text)
for element in element1:
    for a in element.text.split("\n"):
        if (len(a) > 0):
            # print(a, "\n------------------")
            file.write(a+"\n")
    file.write("\n")

file.close()

url = "https://www.nitt.edu/home/academics/departments/cse/faculty/"
r = requests.get(url)
htmlContent = r.content

soup = BeautifulSoup(htmlContent, 'html.parser')

title = soup.title

element1 = soup.find_all(id="side")

file = open("output.txt", "a",encoding='utf-8')
file.write(title.text)
for element in element1:
    for a in element.text.split("\n"):
        if (len(a) > 0):
            # print(a, "\n------------------")
            file.write(a+"\n")
    file.write("\n")

file.close()

url = "https://wsdc.nitw.ac.in/facultynew/dept/faculty_profiles/cse"
r = requests.get(url)
htmlContent = r.content

soup = BeautifulSoup(htmlContent, 'html.parser')

title = soup.title

element1 = soup.find_all(class_="grid-container")

file = open("output.txt", "a",encoding='utf-8')
file.write(title.text)
for element in element1:
    for a in element.text.split("\n"):
        if (len(a) > 0):
            # print(a, "\n------------------")
            file.write(a+"\n")
    file.write("\n")

file.close()



url = "https://minerva.nitc.ac.in/?q=people/faculty&page=1"
r = requests.get(url)
htmlContent = r.content

soup = BeautifulSoup(htmlContent, 'html.parser')

title = soup.title

element1 = soup.find_all(class_="view-content")

file = open("output.txt", "a",encoding='utf-8')
file.write(title.text)
for element in element1:
    for a in element.text.strip().split("\n"):
        if (a.strip()!=""):
            # print(a, "\n------------------")
            file.write(a.replace("\n", "")+"\n")
    file.write("\n")

file.close()

url = "https://minerva.nitc.ac.in/?q=people/faculty&page=2"
r = requests.get(url)
htmlContent = r.content

soup = BeautifulSoup(htmlContent, 'html.parser')

title = soup.title

element1 = soup.find_all(class_="view-content")

file = open("output.txt", "a", encoding='utf-8')
file.write(title.text)
for element in element1:
    for a in element.text.strip().split("\n"):
        if (a.strip()!=""):
            # print(a, "\n------------------")
            file.write(a.replace("\n", "")+"\n")
    file.write("\n")

file.close()

url = "https://minerva.nitc.ac.in/?q=people/faculty&page=3"
r = requests.get(url)
htmlContent = r.content

soup = BeautifulSoup(htmlContent, 'html.parser')

title = soup.title

element1 = soup.find_all(class_="view-content")

file = open("output.txt", "a", encoding='utf-8')
file.write(title.text)
for element in element1:
    for a in element.text.strip().split("\n"):
        if (a.strip()!=""):
            # print(a, "\n------------------")
            file.write(a.replace("\n", "")+"\n")
    file.write("\n")

file.close()


r = requests.get(url)
htmlContent = r.content

soup = BeautifulSoup(htmlContent, 'html.parser')

title = soup.title

element1 = soup.find_all(class_="tab-content")

file = open("output.txt", "a",encoding='utf-8')
file.write(title.text)
for element in element1:
    for a in element.text.split("\n"):
        if (len(a) > 0):
            # print(a, "\n------------------")
            file.write(a+"\n")
    file.write("\n")

file.close()

url = "http://www.manit.ac.in/computer-science-engineering-department-0"
r = requests.get(url)
htmlContent = r.content

soup = BeautifulSoup(htmlContent, 'html.parser')

title = soup.title

element1 = soup.find_all(class_="peoplearea")

file = open("output.txt", "a",encoding='utf-8')
file.write(title.text)
for element in element1:
    for a in element.text.split("\n"):
        if (len(a) > 0):
            # print(a, "\n------------------")
            file.write(a+"\n")
    file.write("\n")

file.close()


url = "https://vnit.ac.in/cse/index.php/faculty/"
r = requests.get(url)
htmlContent = r.content

soup = BeautifulSoup(htmlContent, 'html.parser')

title = soup.title

element1 = soup.find_all(class_="row")

file = open("output.txt", "a",encoding='utf-8')
file.write(title.text)
for element in element1:
    for a in element.text.split("\n"):
        if (len(a) > 0):
            # print(a, "\n------------------")
            file.write(a+"\n")
    file.write("\n")

file.close()

url = "https://website.nitrkl.ac.in/Academics/AcademicDepartments/Faculty.aspx?fgdhwe34=Q1M6Q29tcHV0ZXIgU2NpZW5jZSBhbmQgRW5naW5lZXJpbmc%3d-MBb7wMG%2fNVo%3d"
r = requests.get(url)
htmlContent = r.content

soup = BeautifulSoup(htmlContent, 'html.parser')

title = soup.title

element1 = soup.find_all(class_="blog-page-area sec-spacer")

file = open("output.txt", "a",encoding='utf-8')
file.write(title.text)
for element in element1:
    for a in element.text.split("\n"):
        if (len(a) > 0):
            # print(a, "\n------------------")
            file.write(a+"\n")
    file.write("\n")

file.close()


url = "https://nitandhra.ac.in/dept/cse/faculty"
r = requests.get(url)
htmlContent = r.content

soup = BeautifulSoup(htmlContent, 'html.parser')

title = soup.title

element1 = soup.select('[class~= pull-left]')

file = open("output.txt", "a", encoding='utf-8')
file.write(title.text)
for element in element1:
    r=requests.get(element.get('href'))
    htmlContent=r.content
    soup = BeautifulSoup(htmlContent, 'html.parser')
    el=soup.find_all(class_="panel-body text")
    for i in el:
        file.write(i.text)
    
    file.write("\n")

file.close()

url = "https://www.nitm.ac.in/department/computer-science-engineering/faculty-1"
r = requests.get(url)
htmlContent = r.content

soup = BeautifulSoup(htmlContent, 'html.parser')

title = soup.title

element1 = soup.find_all(class_="row")


file = open("output.txt", "a",encoding='utf-8')
file.write(title.text)
for element in element1:
    for a in element.text.split("\n"):
        if (len(a) > 0):
            # print(a, "\n------------------")
            file.write(a+"\n")
    file.write("\n")

file.close()

url = "https://www.nitnagaland.ac.in/index.php/cse-people/cse-faculty"
r = requests.get(url)
htmlContent = r.content

soup = BeautifulSoup(htmlContent, 'html.parser')

title = soup.title

element1 = soup.find_all(class_="g-block size-84 shadow equal-height")


file = open("output.txt", "a",encoding='utf-8')
file.write(title.text)
for element in element1:
    for a in element.text.split("\n"):
        if (len(a) > 0):
            # print(a, "\n------------------")
            file.write(a+"\n")
    file.write("\n")

file.close()

url = "https://cse.nitsikkim.ac.in/people.php"
r = requests.get(url)
htmlContent = r.content

soup = BeautifulSoup(htmlContent, 'html.parser')

title = soup.title

element1 = soup.find_all(class_="card-board")


file = open("output.txt", "a",encoding='utf-8')
file.write(title.text)
for element in element1:
    for a in element.text.split("\n"):
        if (len(a) > 2):
            # print(a, "\n------------------")
            file.write(a+"\n")
    file.write("\n")

file.close()

url = "https://nita.ac.in/Department/Department_FacultyList.aspx?nDeptID=caasa"
r = requests.get(url)
htmlContent = r.content

soup = BeautifulSoup(htmlContent, 'html.parser')

title = soup.title

element1 = soup.find_all(class_="container")


file = open("output.txt", "a",encoding='utf-8')
file.write(title.text)
for element in element1:
    for a in element.text.split("\n"):
        if (len(a) > 0):
            # print(a, "\n------------------")
            file.write(a+"\n")
    file.write("\n")

file.close()

url = "https://nitdgp.ac.in/department/computer-science-engineering/faculty-1"
r = requests.get(url)
htmlContent = r.content

soup = BeautifulSoup(htmlContent, 'html.parser')

title = soup.title

element1 = soup.find_all(class_="tab-content")


file = open("output.txt", "a",encoding='utf-8')
file.write(title.text)
for element in element1:
    for a in element.text.split("\n"):
        if (len(a) > 0):
            # print(a, "\n------------------")
            file.write(a+"\n")
    file.write("\n")

file.close()

url = "https://www.nitj.ac.in/index.php/nitj_cinfo/index/52"
r = requests.get(url)
htmlContent = r.content

soup = BeautifulSoup(htmlContent, 'html.parser')

title = soup.title

element1 = soup.find_all(class_="table table-bordered table-striped")


file = open("output.txt", "a",encoding='utf-8')
file.write(title.text)
for element in element1:
    for a in element.text.split("\n"):
        if (len(a) > 0):
            # print(a, "\n------------------")
            file.write(a+"\n")
    file.write("\n")

file.close()

url = "https://www.nitsri.ac.in/Pages/FacultyList.aspx?nDeptID=cs"
r = requests.get(url)
htmlContent = r.content

soup = BeautifulSoup(htmlContent, 'html.parser')

title = soup.title

element1 = soup.find_all(class_="gdlr-core-page-builder-body")


file = open("output.txt", "a",encoding='utf-8')
file.write(title.text)
for element in element1:
    for a in element.text.split("\n"):
        if (len(a) > 0):
            # print(a, "\n------------------")
            file.write(a+"\n")
    file.write("\n")

file.close()