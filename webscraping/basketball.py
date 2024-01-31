from bs4 import BeautifulSoup
import requests
import time 
import csv
import pandas as pd
import numpy as np


years = range(2012,2023)
pages = range(1,5)

mydata = pd.DataFrame()


for year in years:

    for page in pages:
    
        headers = []

        source = requests.get(f'https://basketball.realgm.com/ncaa/stats/{year}/Averages/Qualified/All/Season/All/points/desc/{page}/').text

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
        year_df['Year'] = year

        mydata = mydata.append(year_df,ignore_index=True)
        mydata.drop('#', inplace=True, axis=1)
        

    mydata.to_csv(f'college_reg_stats.csv', index=False)
    print(mydata)









    


    
