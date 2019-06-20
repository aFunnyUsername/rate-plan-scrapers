from bs4 import BeautifulSoup
from selenium import webdriver
from splinter import Browser
from selenium.webdriver.support.ui import Select
import pprint
import pandas as pd
import time

def get_browser():
    #GOOGLE_CHROME_BIN = "/app/.apt/usr/bin/google-chrome"
    CHROMEDRIVER_PATH = "chromedriver.exe"

    chrome_options = webdriver.ChromeOptions()

    #chrome_options.binary_location = GOOGLE_CHROME_BIN
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('headless')

    browser = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options)
    return browser

def check_for_existing_supplier(df, supp, href, row_count):
    if supp in df['supplier']:
        if pd.isnull(df[df['suppler'] == supp]['website']):
            df.loc[row_count, 'website'] = href


def get_suppliers():
    browser = get_browser()
    browser.get('https://www.pluginillinois.org/Suppliers.aspx')
    results = browser.page_source
    soup = BeautifulSoup(results, 'html.parser')

    name = 'ctl00$ctl00$ctl00$ctl00$MasterContent$MasterContent$RightColumn$RightColumn$RegistrationList'
    dropdown = soup.find('select', attrs={'name': name})
    dd_options = dropdown.findAll('option')

    options = {}
    for option in dd_options:
        options[option['value']] = option.get_text()

    names_hrefs_df = pd.DataFrame(columns=['supplier', 'website'])
    for option in options:
        browser.implicitly_wait(10)
        select = Select(browser.find_element_by_id('MasterContent_MasterContent_RightColumn_RightColumn_RegistrationList'))
        select.select_by_visible_text(options[option])
        time.sleep(3)
        results = browser.page_source
        time.sleep(3)

        supplier_names = browser.find_elements_by_css_selector('h3.orange')
        spans = browser.find_elements_by_css_selector('span.detail')   

        for i, name in enumerate(supplier_names):
            span = spans[i]
            name = name.text 
            try: 
                a_tag = span.find_element_by_tag_name('a')
                href = a_tag.get_attribute('href') 
            except: 
                href = None
                pass
            if name in names_hrefs_df['supplier']:
                if pd.isnull(names_hrefs_df[names_hrefs_df['supplier'] == name]['website']) and href is not None:
                    names_hrefs_df.loc[i, 'website'] = href 
            else: 
                names_hrefs_df.loc[i, 'supplier'] = name
                names_hrefs_df.loc[i, 'website'] = href
    names_hrefs_df.to_csv('data/names_website.csv')

get_suppliers()






