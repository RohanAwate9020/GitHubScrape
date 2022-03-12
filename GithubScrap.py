from ast import IsNot
import requests
from bs4 import BeautifulSoup


url=input("Please give url:")


r=requests.get(url)
htmlContent=r.content
soup=BeautifulSoup(htmlContent, 'html.parser')


title= soup.title
str1=str(title)
str2=str1.replace('<title>','')
str3=str2.replace('</title>','')
print('\n\n\t\t\t',str3[:-8])


#Displaying Repository name 
j=0
listrepo=[]
print("Repositories Available:")
li=soup.findAll('span', class_='repo')
for _,i in enumerate(li):
   listrepo.append(i.text.strip())
   j=j+1
   print(j,'.',i.text.strip())

print('Number of Repository:',j)
i=0
k=0

for i in range(j):
   urlprj=url+'/'+listrepo[i]
   #print(urlprj)
   print("\nProjects available In",listrepo[i])
   i+=1
  
   r=requests.get(urlprj)
   htmlContent=r.content
   soup=BeautifulSoup(htmlContent, 'html.parser')
   li=soup.findAll('span', class_='css-truncate css-truncate-target d-block width-fit')
   for _,i in enumerate(li):
    strprj=i.text.strip()
    print(strprj)


   li=soup.findAll('a', class_='d-inline-flex flex-items-center flex-nowrap Link--secondary no-underline text-small mr-3')
   print("\nLanguages Used in this Repository")
   for _,i in enumerate(li):
     strlang=i.text.strip()
     print(strlang)
     
   
  




