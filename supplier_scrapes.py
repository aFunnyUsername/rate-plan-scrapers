from bs4 import BeautifulSoup
from splinter import Browser
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import time

###################################################################
##################Scraper Functions for each supplier##############
###################################################################

##############Agera################################################
def agera_scraper(browser, supplier, website, zips_df):
    #browser.implicitly_wait(5)
    #browser.get(website)
    #selectable_service_type = Select(browser.find_element_by_css_selector('select.ctafield'))
    #utility_dict = {}
    #plan_zip_dict = {}
    #for i, zipcode in enumerate(zips_df['zipcode']):
    #    #wait for inputs and button to load
    #    zip_input = WebDriverWait(browser,
    #            10).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, 
    #                'input.ctatext')))
    #    button = WebDriverWait(browser,
    #            10).until(expected_conditions.presence_of_element_located((By.ID,
    #                'getrates')))
    #    zip_input.clear()
    #    zip_input.send_keys(zipcode)
    #    if i == 0: 
    #        browser.execute_script('document.getElementById("customerType").style.display="inline-block";')
    #        selectable_service_type.select_by_visible_text('Residential')

    #    button.click()
    #    #check for plans
    #    if not 'no-plans-found' in browser.current_url:
    #        #check if electricity plans are available
    #        browser.execute_script('document.getElementById("service").style.display="inline-block";')
    #        service_types = Select(browser.find_element_by_css_selector('select.formselect.fieldmarginbt.gasorelec'))
    #        try:
    #            service_types.select_by_visible_text('Electricity')
    #            print('found plans!')
    #            #find and click the new button
    #            new_button = browser.find_element_by_css_selector('button.btn')
    #            new_button.click()
    #            #get the utility name
    #            plan_header = browser.find_element_by_css_selector('div.planheader')
    #            utility = plan_header.find_element_by_css_selector('h2.utilityplan').text[:-6]
    #            print(utility)
    #            #check for utility in the utility dict
    #            if utility not in utility_dict.keys():
    #                #get the plans
    #                plans = browser.find_elements_by_css_selector('div.productplan.electricity')
    #                plan_dict = {}
    #                plan_list = []
    #                plan_zip_dict = {}
    #                for plan in plans: 
    #                    name_div = plan.find_element_by_css_selector('div.col-md-4.col-sm-6.detailsbox')
    #                    name = name_div.find_element_by_tag_name('h1').text

    #                    price_div = plan.find_element_by_css_selector('div.col-md-3.col-sm-6.pricearea')
    #                    price = float(price_div.find_element_by_class_name('price').text[1:])
    #                    unit = price_div.find_element_by_class_name('unit').text

    #                    details_button = plan.find_element_by_class_name('selectdetails')
    #                    details_button.click()

    #                    details_div = plan.find_element_by_css_selector('div.detailsrow.collapse.in')
    #                    description = details_div.find_element_by_css_selector('div.col-md-7.plandetailsbox.detailstext').text
    #                    info_list = details_div.find_elements_by_tag_name('li')
    #                    terms = info_list[0].text
    #                    monthly_fee = info_list[2].text
    #                    enroll_fee = info_list[3].text
    #                    disclosure = info_list[4].find_element_by_tag_name('a').get_attribute('href')
    #                    terms_and_conditions = info_list[5].find_element_by_tag_name('a').get_attribute('href')

    #                    #now, start putting the info into a dictionary
    #                    plan_dict['supplier'] = supplier
    #                    plan_dict['website'] = website
    #                    plan_dict['plan_name'] = name

    #                    pricing_dict = {}
    #                    pricing_dict['price'] = price #                    pricing_dict['unit'] = unit  
    #                    plan_dict['pricing'] = pricing_dict 

    #                    plan_dict['description'] = description

    #                    terms_dict = {}
    #                    terms_dict['term'] = terms
    #                    terms_dict['disclosure'] = disclosure
    #                    terms_dict['terms_and_conditions'] = terms_and_conditions
    #                    plan_dict['terms'] = terms_dict

    #                    fees_dict = {}
    #                    fees_dict['monthly'] = monthly_fee
    #                    fees_dict['enrollment'] = enroll_fee
    #                    plan_dict['fees'] = fees_dict 

    #                    plan_list.append(plan_dict)
    #                plan_zip_dict['plans'] = plan_list
    #                plan_zip_dict['zipcodes'] = [zipcode]
    #                utility_dict[utility] = plan_zip_dict
    #            else:
    #                utility_dict[utility]['zipcodes'].append(zipcode)
    #            browser.back()
    #        except:
    #            print('no electricity plans!')
    #    else:
    #        print('no plans!')
    #    time.sleep(1)
    #    browser.back()
    #    print(utility_dict)
    return None


##############Ambit################################################
def ambit_scraper(browser, supplier, website, zips_df):
    browser.implicitly_wait(5)
    browser.get(website)
    for i, zipcode in enumerate(zips_df['zipcode']):
        #get form spots and enter info
        zip_code_entry = WebDriverWait(browser,
                10).until(expected_conditions.presence_of_element_located((By.ID,
                    'zip')))
        zip_code_entry.clear()
        zip_code_entry.send_keys(zipcode)
        residential_checkbox = WebDriverWait(browser,
                10).until(expected_conditions.presence_of_element_located((By.ID,
                    'residential')))
        residential_checkbox.click()

###########chooser function#######################################
def choose_scraper(browser, supplier, website, zips_df):
    if supplier == 'Agera Energy, LLC':
        agera_scraper(browser, supplier, website, zips_df)
    
    if supplier == 'Ambit Energy':
        ambit_scraper(browser, supplier, website, zips_df)








