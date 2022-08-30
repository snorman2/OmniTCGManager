import pandas as pd # library for data analysis
import requests # library to handle requests
from bs4 import BeautifulSoup # library to parse HTML documents
from pathlib import Path 


series = ['Battle_Brawlers_(Card_set)', 'Bakugan_Resurgence', 'Age_of_Aurelus', 'Armored_Elite', 'Fusion_Force', 'Shields_of_Vestroia','PS1', 'Secrets_of_the_Geogan', 'GG', 'CP', 'EV', 'EV2', 'LE']


i = 0
while i < len(series):

    # get the response in the form of html
    wikiurl="https://bakugan.wiki/wiki/" + series[i]

    response=requests.get(wikiurl)
    print(response.status_code)

    # parse data from the html into a beautifulsoup object
    soup = BeautifulSoup(response.text, 'html.parser')
    target_table=soup.find('table',{'class':"article-table sortable"})  
    print(target_table)
    df=pd.read_html(str(target_table))
    # convert list to dataframe
    df=pd.DataFrame(df[0])
    print(df.head())

    #save csv
    path = 'data/abilitycards/' + series[i] + '.csv'
    filepath = Path(path)  
    filepath.parent.mkdir(parents=True, exist_ok=True)  
    df.to_csv(filepath)  
    i += 1
