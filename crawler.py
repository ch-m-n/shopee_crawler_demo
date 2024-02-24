# from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException

import random
from bs4 import BeautifulSoup
import pandas as pd

from time import sleep

import datetime
import csv
import glob
import os

class Spyder:
    def __init__(self):
        #webdriver option
        self.opt= uc.ChromeOptions()
        # self.opt.add_argument('--no-sandbox') #Disables the sandbox for all process types that are normally sandboxed. Meant to be used as a browser-level switch for testing purposes only.
        # self.opt.add_argument('--headless') #Run in headless mode, i.e., without a UI or display server dependencies.
        # self.opt.add_argument('--disable-notifications')#Disables the Web Notification and the Push APIs.
        # self.opt.add_argument('--window-size=1920,1080')#Get full resolution
        
        # self.opt.add_argument("--proxy-server=%s" % self.PROXY) 

        # self.opt.add_argument("--disable-blink-features=AutomationControlled") 
        # self.opt.add_experimental_option("excludeSwitches", ["enable-automation"]) 
        # self.opt.add_experimental_option("useAutomationExtension", False) 
 
        self.opt.add_experimental_option("detach", True)
        
        # self.driver = uc.Chrome(options=self.opt)
        self.driver = uc.Chrome()
        # self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})") 

        # open browser by webdrive
        self.url = 'https://shopee.vn'
        self.login_url = "https://shopee.vn/buyer/login"
        self.account = os.getenv('ACCOUNT')
        self.password = os.getenv('PASSWORD')

    def get_front_page(self):
        self.driver.get(self.url)

    def get_login_page(self):
        self.driver.get(self.login_url)

    def is_logged_in(self):
        sleep(30)
        try:
            self.driver.find_element(By.CLASS_NAME, 'navbar__username')
        except:
            return False
        return True
    
    def is_comfirm_required(self):
        sleep(8)
        try:
            self.driver.find_element(By.CLASS_NAME, 'dWxniD')
        except:
            return False
        print('Confirmation required, comfirm through email in next 59 second')
        return True
    
    def is_cat_available(self):
        try:
            self.driver.find_element(By.CLASS_NAME,'home-category-list__category-grid')
        except:
            return False
        return True
    
    def clear_popup(self):
        try:
            close_button = self.driver.find_element(By.CLASS_NAME, 'shopee-popup__close-btn')
            close_button.click()
        except:
            pass

    def login(self):
        sleep(random.randint(2,8))
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
        self.driver.get(self.login_url)
        sleep(random.randint(2,8))
        username = self.driver.find_element(By.NAME, "loginKey")
        username.send_keys(self.account)
        sleep(random.randint(2,8))
        password = self.driver.find_element(By.NAME, "password")
        password.send_keys(self.password)
        sleep(random.randint(2,8))
        # self.driver.get_screenshot_as_file("put.png")
        submit_button = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div[2]/div/div[2]/form/button")
        submit_button.click()
        
        if (self.is_comfirm_required()==True):
            self.driver.find_element(By.CLASS_NAME, 'dWxniD').click()

    def get_categories(self):
        sleep(15)
        # self.driver.get(self.url)

        # lg8Hq3
        # header-with-search__logo-section
        list = self.driver.find_elements(By.CLASS_NAME,'home-category-list__category-grid')

        for a in list:
            print(a.get_attribute('href'))

        

if __name__=="__main__": 
    crawl = Spyder()
    # crawl.clear_popup()
    # print(crawl.is_logged_in())
    try:
        crawl.human_speed_login()
        crawl.get_categories()
    except:
        pass
        