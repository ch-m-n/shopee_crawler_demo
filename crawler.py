# The `Spyder` class in the provided Python code is designed to automate web scraping tasks on the
# Shopee website, including logging in, navigating through categories, and extracting product data.
# from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import random
import pandas as pd

from time import sleep
import time
import threading
import logging

import os
from dotenv import load_dotenv
load_dotenv()

import csv
import re
class Spyder:
    def __init__(self):
        #webdriver option
        # self.opt= uc.ChromeOptions()
        # self.opt.add_argument('--no-sandbox') #Disables the sandbox for all process types that are normally sandboxed. Meant to be used as a browser-level switch for testing purposes only.
        # self.opt.add_argument('--headless') #Run in headless mode, i.e., without a UI or display server dependencies.
        # self.opt.add_argument('--disable-notifications')#Disables the Web Notification and the Push APIs.
        # self.opt.add_argument('--window-size=1920,1080')#Get full resolution
        # self.driver = uc.Chrome(options=self.opt)
        self.url = 'https://shopee.vn/'
        self.login_url = "https://shopee.vn/buyer/login"
        self.account = os.getenv('ACCOUNT')
        self.password = os.getenv('PASSWORD')

        self.driver = uc.Chrome()

    def get_front_page(self):
        """
        The function `get_front_page` navigates the web driver to a specified URL.
        """
        self.driver.get(self.url)

    def get_login_page(self):
        """
        The function `get_login_page` navigates the web driver to the login URL.
        """
        self.driver.get(self.login_url)

    def is_logged_in(self):
        """
        The function `is_logged_in` checks if a user is logged in by searching for a specific element on
        the webpage after a delay of 8 seconds.
        :return: The `is_logged_in` method returns `True` if the element with class name
        'navbar__username' is found on the page, indicating that the user is logged in. If the element
        is not found, it returns `False`, indicating that the user is not logged in.
        """
        sleep(8)
        try:
            self.driver.find_element(By.CLASS_NAME, 'navbar__username')
        except:
            return False
        return True
    
    def is_comfirm_required(self):
        """
        This Python function checks if confirmation is required by looking for a specific element and
        returns True if confirmation is needed.
        :return: The function `is_confirm_required` returns a boolean value - `True` if confirmation is
        required and `False` if confirmation is not required.
        """
        sleep(8)
        try:
            self.driver.find_element(By.CLASS_NAME, 'dWxniD')
        except:
            return False
        print('Email confirmation required, comfirm through email in next 59 second')
        return True
    
    def login(self):
        """
        The `login` function in the Python code snippet automates the login process by entering the
        username and password, clicking the submit button, and handling a confirmation prompt if
        required.
        """
        self.driver.get(self.login_url)
        username = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.NAME, "loginKey"))).send_keys(self.account)
        password = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.NAME, "password"))).send_keys(self.password)
        # self.driver.get_screenshot_as_file("put.png")
        submit_button = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
            (By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div[2]/div/div[2]/form/button"))).click()
        
        if (self.is_comfirm_required()==True):
            self.driver.find_element(By.CLASS_NAME, 'dWxniD').click()
            sleep(59)
                    
    def human_speed_login(self):
        """
        The function `human_speed_login` automates the login process on a website with human-like delays
        and interactions.
        """
        self.driver.get(self.login_url)
        sleep(random.randint(3,8))
        username = self.driver.find_element(By.NAME, "loginKey")
        username.send_keys(self.account)
        sleep(random.randint(3,8))
        password = self.driver.find_element(By.NAME, "password")
        password.send_keys(self.password)
        sleep(random.randint(3,8))
        # self.driver.get_screenshot_as_file("put.png")
        submit_button = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div[2]/div/div[2]/form/button")
        submit_button.click()
        
        if (self.is_comfirm_required()==True):
            self.driver.find_element(By.CLASS_NAME, 'dWxniD').click()
            sleep(59)
                
    def view_data(self, tag):
        """
        The `view_data` function collects product data from a webpage, processes it, and saves it to a
        CSV file.
        
        :param tag: The `tag` parameter in the `view_data` method is used as a label to identify the
        data being processed. It is used to name the CSV file that will be created with the extracted
        data
        """
        data = {'product_name':[], 'product_url':[], 'product_rating':[], 'product_price':[], 'product_revenue':[]}
        sleep(10)
        total_products = self.driver.find_elements(By.CLASS_NAME, "shopee-search-item-result__item")

        for product in total_products:
            total_sell = product.find_element(By.CLASS_NAME,'OwmBnn').text
            total_sell = total_sell.replace(',', '.')
            num = [float(num) for num in re.findall(r'[\d.]+', total_sell)]
            sell_num = 0       
            if(total_sell.endswith('k')):
                sell_num = num[0]*1000
            prices = product.find_elements(By.CLASS_NAME,'IWBsMB')
            possible_price = 0
            for price in prices:
                multi_price = price.find_elements(By.CLASS_NAME,'k9JZlv')
                if(len(multi_price)>1):
                    possible_price = multi_price[1].text
                    possible_price = float(possible_price.replace('.', ''))
                if(len(multi_price)==1):
                    possible_price = multi_price[0].text
                    possible_price = float(possible_price.replace('.', ''))

            stars = product.find_elements(By.CLASS_NAME,'shopee-rating-stars__lit')
            rating = 0
            rate = "{:.2f}".format(rating)
            for star in stars:
                value = star.get_attribute('style')
                value = value.split(":")
                value = value[1].split(";")
                value = value[0].split("%")
                value = value[0]
                if(value==100):
                    rating += 1.0
                else:
                    rating += float(value)/100
            data['product_name'].append(product.find_element(By.CLASS_NAME,'DgXDzJ').text)
            data['product_url'].append(product.find_element(By.TAG_NAME,'a').get_attribute('href'))
            data['product_rating'].append(rate)
            data['product_price'].append(possible_price)
            data['product_revenue'].append(sell_num*possible_price)
        print(data)
        df = pd.DataFrame(data)
        df.to_csv('.\\data\\'+str(tag)+'_products.csv', sep='\t', encoding='utf-8', index=False)

    def crawling(self):
        """
        The function crawls through a website, extracts category links, navigates through pages, and
        collects data.
        """
        cat = []
        sleep(10)
        list = self.driver.find_elements(By.CLASS_NAME,'home-category-list__category-grid')
        print('Listing categories')
        for a in list:
            cat.append(a.get_attribute('href'))
        
        for link in cat:
            self.driver.get(link)
            sleep(10)

            total_page = self.driver.find_element(By.CLASS_NAME, "shopee-mini-page-controller__total").text
            current_page = self.driver.find_element(By.CLASS_NAME, "shopee-mini-page-controller__current").text
            while int(current_page) < int(total_page):
                self.view_data(re.findall(r'\d+', link )[0])
                self.driver.get(link+'?page='+str(int(current_page)+1))

            sub_cat = self.driver.find_elements(By.CLASS_NAME, "shopee-category-list__sub-category")
            for sub in sub_cat:
                self.driver.get(sub.get_attribute('href'))
                while int(current_page) < int(total_page):
                    self.view_data(re.findall(r'\d+', link )[0])
                    self.driver.get(link+'?page='+str(int(current_page)+1))

if __name__=="__main__": 
    crawl = Spyder()
    crawl.human_speed_login()
    crawl.crawling()