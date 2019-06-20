import pprint
import pandas as pd
import time
import supplier_scrapes
from selenium import webdriver

def get_browser():
    #GOOGLE_CHROME_BIN = "/app/.apt/usr/bin/google-chrome"
    CHROMEDRIVER_PATH = "chromedriver.exe"

    chrome_options = webdriver.ChromeOptions()

    #chrome_options.binary_location = GOOGLE_CHROME_BIN
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    #chrome_options.add_argument('headless')

    browser = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options)
    return browser

def get_websites():
    websites_df = pd.read_csv('data/names_website.csv')
    usable_sites_df = websites_df[websites_df['useorno'] == 'yes'][[
        'supplier', 'website']]
    return usable_sites_df

def get_zipcodes():
    zipcodes_df = pd.read_csv('data/zips.csv')
    return zipcodes_df

def get_plans():
    sites_df = get_websites()
    zips_df = get_zipcodes()
    browser = get_browser()
    #loop through the different suppliers
    for row in sites_df.iterrows():
        supplier = row[1]['supplier']
        website = row[1]['website']
        supplier_scrapes.choose_scraper(browser, supplier, website, zips_df)

get_plans()





