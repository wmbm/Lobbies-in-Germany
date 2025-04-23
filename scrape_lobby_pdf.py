from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import json
import numpy as np
import os
import glob
import time
from datetime import datetime

def setup_folders(data_dir, base_directory = 'lobby_germany/PDFs/', clear_all=True):
    """
    Create directory structure for organizing petition data.

    Parameters:
    data_dir (str): The root directory where the data folders will be created.
    base_directory (str, optional): The base directory name (default is 'petitions_website/').
    state (str, optional): The state or category name to append to the base directory (default is 'all').
    clear_all (bool): Remove previously downloaded files

    Returns:
    str: The path to the created data directory.
    """

    # Create child directory
    data_path = os.path.join(data_dir, base_directory)
    if not os.path.exists(data_path):
        os.makedirs(data_path)
    
    # Get current date
    current_date = datetime.today().strftime('%Y-%m-%d')
    
    directory = base_directory + current_date + '/'
    data_path = os.path.join(data_dir, directory)
    if not os.path.exists(data_path):
        os.mkdir(data_path)

    if clear_all:
        files = glob.glob(data_path + '/*')
        for f in files:
            os.remove(f)
    return data_path

def setup_browser_bot(data_path, headless=False, browser='chrome'):
    """
    data_path   : location to save petition json data
    headless    : whether or not you seen the browser popup
    browser     : which browser (Chrome currently only setup)
    """
    
    if browser == 'firefox':
        from selenium.webdriver.firefox.service import Service
        browser = webdriver.Firefox(options=options)
        # To prevent download dialogue
        options.set_preference('browser.download.folderList', 2) # custom location
        options.set_preference('browser.download.manager.showWhenStarting', False)
        options.set_preference('browser.download.dir', data_path)
        options.set_preference('browser.helperApps.neverAsk.saveToDisk', 'text/csv')
        # Headless is faster
        if headless:
            options.add_argument("--headless")

    
    elif browser == 'chrome':
        from selenium.webdriver.chrome.service import Service
        options = webdriver.ChromeOptions()
        
        # To prevent download dialogue & specify download folder
        options.add_experimental_option('prefs', {
            'download.default_directory': data_path,
            'download.prompt_for_download': False,
            'download.directory_upgrade': True,
            'safebrowsing.enabled': True,
            'plugins.always_open_pdf_externally': True
        })
        
        # Headless is faster
        if headless:
            options.add_argument("--headless")

        # Prevent misc error
        options.add_argument("--remote-debugging-port=9230")

        # Check if Chrome driver exists before creating the WebDriver instance
        chromedriver_path = os.path.abspath('./chromedriver-linux64/chromedriver')

        if os.path.exists(chromedriver_path):
            service = Service()#executable_path=chromedriver_path)
            browser = webdriver.Chrome(service=service, options=options)
        else:
            print(f"File not found: {chromedriver_path}")

    else:
        print('Browser not supported')

    return browser



"""
Chromium Version 124.0.6367.60 
Chrome driver Version 124.0.6367.60

"""
# Parameters
data_dir = '/home/will/Datasets/' # should exist already on your computer
data_path = setup_folders(data_dir)
print(f"Location of scraped PDFs: {data_path}")

# Setup browser
browser = setup_browser_bot(data_path, headless=False, browser='chrome')

# Open FIRST page
browser.get('https://www.lobbyregister.bundestag.de/suche?sort=REGISTRATION_DESC&pageSize=100')
page_count = browser.find_element('xpath', '/html/body/main/div/div[3]/div/div/div/div/div[1]/div[4]/div/div/div[1]/ul/li[8]/a') # Needs try-except

# Find number of pages
n_pages = int(page_count.text.split("\n")[1])
print(f"Number of pages found: {n_pages}")

# Find & click download button 
button_xpath = '/html/body/main/div/div[3]/div/div/div/div/div[1]/div[2]/div[2]/div/div/div/div/div[2]/a'
button = browser.find_element('xpath', button_xpath) # Needs try-except
button.click()

# Loop through OTHER pages and scrape petition data
for i in np.arange(2, n_pages + 1, 1):
    # Go to next page
    browser.get(f'https://www.lobbyregister.bundestag.de/suche?pageSize=100&sort=REGISTRATION_DESC&page={i}')

    # Find & click download button
    button = browser.find_element('xpath', button_xpath) # Needs try-except
    button.click()
    time.sleep(3)
    

browser.close()