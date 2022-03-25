from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

taro_ki_link = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'

page = requests.get(taro_ki_link)

soup = bs(page.text,'html.parser')

star_table = soup.find_all('table')

temp_list= []

taro_ki_table = star_table[7].find_all('tr')

for tr in taro_ki_table:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)

Taro_ke_nam = []
Distance =[]
Mass = []
Radius =[]


for i in range(1,len(temp_list)):
    
    Taro_ke_nam.append(temp_list[i][0])
    Distance.append(temp_list[i][5])
    Mass.append(temp_list[i][7])
    Radius.append(temp_list[i][8])

df2 = pd.DataFrame(list(zip(Taro_ke_nam,Distance,Mass,Radius,)),columns=['Star_name','Distance','Mass','Radius'])
print(df2)

df2.to_csv('dwarf_stars.csv')
