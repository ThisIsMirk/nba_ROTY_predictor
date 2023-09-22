from bs4 import BeautifulSoup
import requests
import time 
import csv
import pandas as pd
import numpy as np


players = []
current_rookies = 'currentrookies.csv'

with open(current_rookies, 'r') as file:
    csv_reader = csv.reader(file)

    for row in csv_reader:
        name = row[0]
        players.append(name)


mydata = pd.DataFrame()


# for player in players:

#     for page in pages:
    
headers = []

source = requests.get('https://basketball.realgm.com/player/Victor-Wembanyama/International/136048/2023/By_Season/Advanced_Stats/0/All_Leagues').text

soup = BeautifulSoup(source, 'lxml')
player_info = soup.find('table')

for header in player_info.find_all('th'):
    title = header.text
    headers.append(title)

row_data = []

for j in player_info.find_all('tr')[1:]:
    row_data = j.find_all('td')
    row = [header.text for header in row_data]
    row_data.append(row)

df_player = pd.DataFrame(row_data, columns=headers)
mydata = mydata.append(df_player, ignore_index=True)



print(mydata)

#mydata.to_csv(f'college_reg_stats.csv', index=False)










    


    
