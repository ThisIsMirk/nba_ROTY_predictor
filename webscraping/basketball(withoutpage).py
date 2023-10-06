from bs4 import BeautifulSoup
import requests
import time 
import csv
import pandas as pd


years = range(2012,2023)
pages = range(1,25)

for year in years:  
    headers = []
    source = requests.get(f'https://basketball.realgm.com/ncaa/stats/{year}/Advanced_Stats/Qualified/All/Season/All/per/desc/1/').text

    soup = BeautifulSoup(source, 'lxml')
    player_info = soup.find('table')

    for header in player_info.find_all('th'):
        title = header.text
        headers.append(title)

    mydata = pd.DataFrame(columns=headers)

    for j in player_info.find_all('tr')[1:]:
        row_data = j.find_all('td')
        row = [header.text for header in row_data]
        length = len(mydata)
        mydata.loc[length] = row

    mydata.drop('#', inplace=True, axis=1)
    mydata.to_csv(f'college_adv_stats({year}).csv', index=False)

    print(mydata)









    


    
