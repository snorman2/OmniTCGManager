import os
import pandas as pd # library for data analysis
import requests # library to handle requests
from bs4 import BeautifulSoup # library to parse HTML documents
from pathlib import Path 
import shutil


def write_file(file_destination: str, content: bytes):
    with tempfile.NamedTemporaryFile() as fp:
        fp.write(content)
        fp.flush()
        shutil.copy(fp.name, file_destination)
    
series = ['Battle_Brawlers_(Card_set)', 'Bakugan_Resurgence', 'Age_of_Aurelus', 'Armored_Elite', 'Fusion_Force', 'Shields_of_Vestroia','PS1', 'Secrets_of_the_Geogan', 'GG', 'CP', 'EV', 'EV2', 'LE']


i = 0
while i < len(series):

    # get the response in the form of html
    baseURL = "https://bakugan.wiki"
    wikiurl="https://bakugan.wiki/wiki/" + series[i]

    response=requests.get(wikiurl)
    print(response.status_code)

    # parse data from the html into a beautifulsoup object
    soup = BeautifulSoup(response.text, 'html.parser')
    cardImages=soup.find_all('a', attrs={'class':'image'})
    
    links = []

    for card in cardImages:
        links.append(card.get('href'))
    
    print("All links obtained. Pulling images for " + series[i] + "...")

    count = 0
    #modify the urls to the right
    while count < len(links):
      link = links[count]
      cardListURL=baseURL+link
      print("navigating to " + baseURL + link + "...")
      
      #navigate to the set 
      r=requests.get(cardListURL)
      print(r.status_code)
      cardSource = BeautifulSoup(r.text, 'html.parser')
      cardImage = cardSource.find('div', {'class':'fullImageLink'})
      sourceURL = cardImage.find('a').get('href')
      print("Card source url is " + sourceURL)

      #pull the url for the FILE location page on wiki and create file name based on same file name from site
      imageSource = baseURL + sourceURL
      filename = imageSource.split("/")[-1]
      print("navigating to " + imageSource + "...")

      #navigate to the FILE wiki page
      imageRequest=requests.get(cardListURL)
      print(imageRequest.status_code)
      if imageRequest.status_code == 200:

        #grab the source URL for the actual file location
        imageSoup = BeautifulSoup(imageRequest.text, 'html.parser')
        image = imageSoup.find('div', {'class':'fullImageLink'})
        imageURL = baseURL + image.find('a').get('href')

        #request the file and write it to local
        with open (filename, 'wb') as f:
          im = requests.get(imageURL)
          f.write(im.content)
          print('file saved successfully')
      else:
        print('Image Couldn\'t be retreived')

      count += 1
    i += 1

    