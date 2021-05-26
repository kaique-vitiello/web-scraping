# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 12:30:26 2021

@author: Kaique
"""

from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep

url = 'https://www.oi.com.br/minha-oi/102busca/'

driver = webdriver.Chrome(executable_path='C:/Users/Kaique/Downloads/chromedriver_win32/chromedriver.exe')
driver.get(url)

sleep(5)
driver.find_element_by_id('negocio').click()
sleep(1)
driver.find_element_by_id('input-nome-razao-social').send_keys('oao')
sleep(1)
driver.find_element_by_css_selector('[placeholder="UF"]').send_keys('rs')
sleep(1)
driver.find_element_by_xpath('//button[@value="RS"]').click()
sleep(1)
driver.find_element_by_css_selector('[placeholder="Cidade"]').send_keys('porto alegre')
sleep(1)
driver.find_element_by_xpath('//button[@value="Porto Alegre"]').click()
sleep(2)
driver.find_element_by_class_name('btn').click()