# predicting-roty-nba
Contributors: Mirza Abubacker and Shaheryar Haider\
Tools used: Python (BeautifulSoup, sklearntree), PowerBI\
(This README was not generated using an LLM, instead it was written by hand by Mirza) 

## NBA Rookie of the Year Prediction (Ongoing)
Mirza and Shay's journey to learn webscraping and machine learning through project-based learning starts here. Through their combined interest in basketball and data analysis, we find ourselves at a crossroads. 
After much brainstorming that entertained ideas of predicting this seaason's MVP, best player in each position etc., Shay had the brilliant idea of predicting this year's Rookie of the Year (ROTY) using data from players' college basketball stats. 

We knew that there would be a significant amount of data collection involved before we could start working on the machine learning. There were several basketball statistics websites with detailed data collection on college basketball players that included advanced stats that we could pull data from. However, none of these websites had the option to export formatted data in the way that we wanted, this meant we would have to dabble in webscraping to get what we wanted. 

### Webscraping Using BeautifulSoup
We decided we would use 10 years worth of data, mostly because it was a nice spot between too little data and too much data (to clean and organize). Using RealGM as our main source of data we got to work on writing the code for webscraping using BeautifulSoup 

