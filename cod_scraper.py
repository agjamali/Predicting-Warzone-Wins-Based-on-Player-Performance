# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 03:48:07 2020

@author: ali_e

Goals:
    
1. Extract name, player, platform and value for metric for 1 page.

2. Figure out where to store the above data.

3. Figure out how to go to the next page.

4. Repeat steps 1-3.

After, need to get other metrics (figure out which ones are needed).

Then, need a way to match the metric to the player and only have 1 instance of their name.
"""

import requests
from bs4 import BeautifulSoup

#custom functions needed for scraping saved here
import scraper_functions as sf

url = 'https://cod.tracker.gg/warzone/leaderboards/battle-royale/all/Wins?page='


for num in range(1,11):
    
    #getting page number
    page_num = str(num)
    
    page = requests.get(url + page_num)
    
    soup = BeautifulSoup(page.content, 'html.parser')
    
    # ----------------------------------------------------------------------------
    # Need to select row and extract console, player name, wins and Matches Played
    
    #each row of player data has a tr tag
    data = soup.find_all('tr')
    #removing first row which is just the table heading
    del data[0]
    
    win_data = sf.get_wins(data)

































