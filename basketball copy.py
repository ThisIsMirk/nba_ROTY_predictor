from bs4 import BeautifulSoup
import requests
import time 
import csv
import pandas as pd
import numpy as np


years = 2023
pages = range(1,21)

mydata = pd.DataFrame()




for page in pages:

    headers = []

    source = requests.get(f'https://basketball.realgm.com/ncaa/stats/{years}/Advanced_Stats/Qualified/All/Season/All/per/desc/{page}/').text

    soup = BeautifulSoup(source, 'lxml')
    player_info = soup.find('table')

    for header in player_info.find_all('th'):
        title = header.text
        headers.append(title)
    
    year_data = []

    for j in player_info.find_all('tr')[1:]:
        row_data = j.find_all('td')
        row = [header.text for header in row_data]
        year_data.append(row)

    year_df = pd.DataFrame(year_data, columns=headers)
    year_df['Year'] = years

    mydata = mydata.append(year_df,ignore_index=True)
    mydata.drop('#', inplace=True, axis=1)
        

    mydata.to_csv(f'current_rookie_stats.csv', index=False)
    print(mydata)









    


    
