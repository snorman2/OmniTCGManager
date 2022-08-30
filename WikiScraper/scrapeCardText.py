import pandas as pd # library for data analysis
import requests # library to handle requests
from bs4 import BeautifulSoup # library to parse HTML documents
from pathlib import Path 
import numpy as np


i = 0
csvs = ['Battle_Brawlers_(Card_set).csv','Bakugan_Resurgence.csv','Age_of_Aurelus.csv','Armored_Elite.csv', 'Fusion_Force.csv','Shields_of_Vestroia.csv','PS1.csv', 'Secrets_of_the_Geogan.csv', 'GG.csv','EV.csv', 'EV2.csv', 'LE.csv']

while i < len(csvs):
    filename = "./data/abilitycards/" + csvs[i]
    df = pd.read_csv(filename, usecols = ['Card Name'])
    #convert datafram to an array and replace all empty spaces with underscores
    card_list = df['Card Name'].to_numpy()
    converter = lambda x: x.replace(' ', '_')
    new_card_list = list(map(converter, card_list))
    print(new_card_list)
    #wiki url includes the set suffix always and not all card names include the suffix, add the suffix to the card name if the card name doesn't have it

    series = ['_(Battle_Brawlers)','_(Bakugan_Resurgence)','_(Age_of_Aurelus)','_(Armored_Elite)','_(Fusion_Force)','_(Shields_of_Vestroia)','_(Brawler_Pack)','_(Secrets_of_the_Geogan)','_(GG)','_(EV)','_(EV2)','_(LE)']
    j = 0
    print('GETTING CARDS FOR SERIES : ' + csvs[i])
    while j < len(new_card_list):
        if series[i] not in new_card_list[j]:
            new_card_list[j] = new_card_list[j] + series[i] 
           
        j += 1

    card_text = []
    k = 0
    while k < len(new_card_list):
        #navigate to card page and pull the card text
        wikiurl="https://bakugan.wiki/wiki/" + new_card_list[k]

        print("naviagating to page: " + wikiurl)
        count = 0
        response=requests.get(wikiurl)
        print(response.status_code)
        target_td = ""
        if response.status_code == 404:
            count += 1
            wikiurl = wikiurl.replace(series[i], '')
            print("naviagating to page: " + wikiurl)
            response_retry=requests.get(wikiurl)
            print(response_retry.status_code)
            if response_retry.status_code == 404:
                print("Card not found")
                target_td = "Card not found"
                card_text.append(target_td)
            if response_retry.status_code == 200:
                print("Card found")
                soup = BeautifulSoup(response_retry.text, 'html.parser')
                target_td=soup.find('td',{'colspan':"3"})
                card_text.append(target_td)
        if response.status_code == 200:
            print("Card found")
            soup = BeautifulSoup(response.text, 'html.parser')
            target_td=soup.find('td',{'colspan':"3"})
            card_text.append(target_td)
        k += 1

    print(card_text)

    export_arry = np.array(card_text)
    df = pd.DataFrame(card_text, columns = ['Text'])
    print(df.head())

    #save csv
    path = 'data/abilitycards/' + series[i] + '_Card_Text.csv'
    filepath = Path(path)  
    filepath.parent.mkdir(parents=True, exist_ok=True)  
    df.to_csv(filepath) 
    i+=1