import pandas as pd # library for data analysis
import requests # library to handle requests
from bs4 import BeautifulSoup # library to parse HTML documents
from pathlib import Path 
import numpy as np

df = pd.read_csv("./data/abilitycards/Battle_Brawlers.csv", usecols = ['Card Name'])
#convert datafram to an array and replace all empty spaces with underscores
card_list = df['Card Name'].to_numpy()
converter = lambda x: x.replace(' ', '_')
new_card_list = list(map(converter, card_list))

#wiki url includes the set suffix always and not all card names include the suffix, add the suffix to the card name if the card name doesn't have it
series = '_(Battle_Brawlers)'
i = 0
while i < len(new_card_list):
        if series not in new_card_list[i]:
            new_card_list[i] = new_card_list[i] + series 
           
        i += 1

print(new_card_list)


#navigate to card page and pull the card text
wikiurl="https://bakugan.wiki/wiki/" + new_card_list[0]

print("naviagating to page: " + wikiurl)

response=requests.get(wikiurl)
print(response.status_code)

soup = BeautifulSoup(response.text, 'html.parser')
target_td=soup.find('td',{'colspan':"3"})

print(target_td)

