from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
#import pyautogui as pg
from selenium.webdriver.support import expected_conditions as EC
import sys

import time
from selenium.webdriver.common.keys import Keys
PATH='/home/tangobeer/Documents/chromedriver'

mailid=input('Enter mail id')
mail_pass=input('ENter password')


print("Enter the message to be bulk sent")
MESSAGE = input()
print(MESSAGE)
# creating an empty list 
EMAILS = [] 
  
# number of elemetns as input 
NUM_OF_MAILS=int(input("Enter number of mails to be sent: "))
  
# iterating till the range 
for i in range(0, NUM_OF_MAILS): 
    ele = input("Please enter the mail address") 
    EMAILS.append(ele) # adding the element 

print(EMAILS)

# write a gmail opening script
driver=webdriver.Chrome(PATH)
driver.get('https://mail.protonmail.com/inbox?welcome=true')
driver.implicitly_wait(5)
txt_box_in_mail=driver.find_element_by_id("username")
txt_box_in_mail.send_keys(mailid)
pass_in_mail=driver.find_element_by_id("password")
pass_in_mail.send_keys(mail_pass)
driver.maximize_window()
pass_in_mail.send_keys(Keys.RETURN)

driver.implicitly_wait(3)
time.sleep(5)

for i in range (0, NUM_OF_MAILS):
    COMPOSE=driver.find_element_by_xpath("//*[contains(text(), 'Compose')]")
    COMPOSE.click()
    driver.implicitly_wait(3)
    mail_to=driver.find_element_by_name("autocomplete")
    mail_to.send_keys(EMAILS[i])
    mail_subject=driver.find_element_by_xpath("//input[@title-translate-context='info']")
    mail_subject.send_keys("ANother twst")
    iframe = driver.find_element_by_tag_name('iframe')
    driver.switch_to.frame(iframe)
    mail_content=driver.find_element_by_xpath("//div")
    mail_content.send_keys(MESSAGE)
    driver.switch_to.default_content()
    SEND=driver.find_element_by_xpath("//*[contains(text(), 'Send')]")
    SEND.click()
    time.sleep(5)

driver.implicitly_wait(2)
driver.quit()
