import pandas as pd # library for data analysis

from bs4 import BeautifulSoup # library to parse HTML documents
from pathlib import Path 
import numpy as np


i = 0
csvs = ['Battle_Brawlers_(Card_set).csv','Bakugan_Resurgence.csv','Age_of_Aurelus.csv','Armored_Elite.csv', 'Fusion_Force.csv','Shields_of_Vestroia.csv','PS1.csv', 'Secrets_of_the_Geogan.csv', 'GG.csv','EV.csv', 'EV2.csv', 'LE.csv', 'CP.csv']

    
filename = "./data/abilitycards/" + csvs[i]
df = pd.read_csv(filename, dtype=str)
#convert datafram to an array and replace all empty spaces with underscores
text_list = df['Text'].to_numpy()


print(type(text_list[0]))
print(text_list[0])
text_list[0] = text_list[0].replace('<td colspan="3">', "lol you've been replaced")
print("REPLACED: " + text_list[0])
i+=1


 

