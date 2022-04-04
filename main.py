from turtle import goto
from selenium import webdriver
import time
import os


print("DooGrade TBS School")
print("Made By ???")
print("Web Doo grade maeng kak that why i code this lmao")

print("Your Student Number Please >")
STUDENTNUM = input()

print("Birthday ex. 04/05/2556 >")
BD = input()    

web = webdriver.Chrome()
web.get('http://122.155.132.196/Semester2551/')


print("Error Checking")
if (web.find_element_by_xpath('/html/body/form/div[3]/div[2]/div/table/tbody/tr[1]/td[3]/input')):
    print("No Error caught") 
else: 
    print("Error Refreshing")
    web.Refresh()

stunum = web.find_element_by_xpath('/html/body/form/div[3]/div[2]/div/table/tbody/tr[1]/td[3]/input')
stunum.send_keys(STUDENTNUM)

BDD = web.find_element_by_xpath('/html/body/form/div[3]/div[2]/div/table/tbody/tr[2]/td[2]/input')
BDD.send_keys(BD)

Submit = web.find_element_by_xpath('/html/body/form/div[3]/div[2]/div/input')
Submit.click()
