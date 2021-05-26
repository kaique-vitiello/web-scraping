# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 12:30:26 2021

@author: Kaique
"""
from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
from python_anticaptcha import AnticaptchaClient, ImageToTextTask

url = 'https://consulta-crf.caixa.gov.br/consultacrf/pages/consultaEmpregador.jsf'

driver = webdriver.Chrome(executable_path='/home/kvl/git/web_scraping/chromedriver')
driver.get(url)

sleep(5)
driver.find_element_by_xpath('//*[@id="mainForm:txtInscricao1"]').send_keys('02558074')
#sleep(1)
#driver.find_element_by_css_selector('//*[@id="tbl"]/tbody/tr/td[3]/div/div/span').send_keys('') #selecionar UF



# bypassing captcha image 
api_key = 'da2b6e2c9c2455151467e85bdaf7779d'
captcha = driver.find_element_by_xpath('//*[@id="captchaImg_N2"]').get_attribute('src')
captcha_fp = open(captcha, 'r')
client = AnticaptchaClient(api_key)
task = ImageToTextTask(captcha_fp)
job = client.createTask(task)
job.join()
print (job.get_captcha_text())

'''
captcha = driver.find_element_by_id("mainForm:txtCaptcha") #preencher campo com captcha resolvido
captcha.send_keys(result['solution']['text'])
'''


sleep(1)
driver.find_element_by_xpath('//*[@id="mainForm:btnConsultar"]').click()