import pandas as pd # library for data analysis
import requests # library to handle requests
from bs4 import BeautifulSoup # library to parse HTML documents
from pathlib import Path 

# get the response in the form of html
wikiurl="https://bakugan.wiki/wiki/Battle_Brawlers_(Card_set)"

response=requests.get(wikiurl)
print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
target_table=soup.find('table',{'class':"article-table sortable"})  

df=pd.read_html(str(target_table))
# convert list to dataframe
df=pd.DataFrame(df[0])
print(df.head())

#save csv

filepath = Path('data/abilitycards/Battle_Brawlers.csv')  
filepath.parent.mkdir(parents=True, exist_ok=True)  
df.to_csv(filepath)  

