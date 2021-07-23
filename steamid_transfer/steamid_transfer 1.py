import selenium
from selenium import webdriver
import time
from pathlib import Path
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random


webdriver_path = Path("chromedriver.exe")
webdriver_path1 = Path("chromedriver.exe")

driver = webdriver.Chrome(webdriver_path)
driver1 = webdriver.Chrome(webdriver_path)

random_id = ""
juu1 = ["a","b","c","d","j","u","i","A","E","1","2","3","4","5","6","7","8","9"]


for x in range(30):
    gg = random.choice(juu1)
    random_id += gg

print(random_id)    


steam_acc_and_password = open("steamid_username_password_ensimmäinen.txt")
steam_acc_and_password_another = open("steamid_username_password_toinen.txt")

if_steamguard = open("jos_steamguard.txt")
if_steamguard1 = open("jos_steamguard2.txt")

if_steamguard_string = if_steamguard.readlines()
if_steamguard_string1 = if_steamguard1.readlines()

print(if_steamguard_string1)

steam_acc_and_password1 = steam_acc_and_password.readlines()
steam_acc_and_password2 = steam_acc_and_password_another.readlines()

steam_acc_and_password3 = []
steam_acc_and_password4 = []

list_length1 = len(steam_acc_and_password1)
list_length2 = len(steam_acc_and_password2)

driver.get("https://store.steampowered.com/login/?l=finnish")
driver1.get("https://store.steampowered.com/login/?l=finnish")

for g in range(list_length1):
    bbb = steam_acc_and_password1[g].replace("\n","")
    steam_acc_and_password3.append(bbb)

for g in range(list_length2):
    bbb = steam_acc_and_password2[g].replace("\n","")
    steam_acc_and_password4.append(bbb)


def first_account():
    element = driver.find_element_by_xpath("/html/body/div[1]/div[7]/div[4]/div/div/div[1]/div/div/div/div/form/div[1]/input")
    element.click()
    element.send_keys(steam_acc_and_password3[0])
    element = driver.find_element_by_xpath("/html/body/div[1]/div[7]/div[4]/div/div/div[1]/div/div/div/div/form/div[2]/input")
    element.click()
    time.sleep(0.1)
    element.send_keys(steam_acc_and_password3[1])
    element = driver.find_element_by_xpath("/html/body/div[1]/div[7]/div[4]/div/div/div[1]/div/div/div/div/div[3]/div[1]/button/span")
    element.click()
    if if_steamguard_string == "True" or if_steamguard_string == "true":
        zzz = input("mikä on koodi: ")
        element = driver.find_element_by_xpath("/html/body/div[3]/div[3]/div/div/div/form/div[3]/div[1]/div/input")
        time.sleep(0.1)
        element.send_keys(zzz)
        element = driver.find_element_by_xpath("/html/body/div[3]/div[3]/div/div/div/form/div[4]/div[1]/div[1]")
        element.click()
    time.sleep(2)
    driver.get("http://steamcommunity.com/my/profile")
    time.sleep(0.2)
    element = driver.find_element_by_xpath("/html/body/div[1]/div[7]/div[6]/div[1]/div[1]/div/div/div/div[3]/div[2]/a")
    element.click()

def second_account():
    element1 = driver1.find_element_by_xpath("/html/body/div[1]/div[7]/div[4]/div/div/div[1]/div/div/div/div/form/div[1]/input")
    element1.click()
    element1.send_keys(steam_acc_and_password2[0])
    element1 = driver1.find_element_by_xpath("/html/body/div[1]/div[7]/div[4]/div/div/div[1]/div/div/div/div/form/div[2]/input")
    element1.click()
    time.sleep(0.1)
    element1.send_keys(steam_acc_and_password2[1])
    element1 = driver1.find_element_by_xpath("/html/body/div[1]/div[7]/div[4]/div/div/div[1]/div/div/div/div/div[3]/div[1]/button/span")
    element1.click()
    if if_steamguard_string1[0] == "True" or if_steamguard_string1[0] == "true":
        zzz = input("mikä on koodi: ")
        element1 = driver1.find_element_by_xpath("/html/body/div[3]/div[3]/div/div/div/form/div[3]/div[1]/div/input")
        time.sleep(0.1)
        element1.send_keys(zzz)
        element1 = driver1.find_element_by_xpath("/html/body/div[3]/div[3]/div/div/div/form/div[4]/div[1]/div[1]")
        element1.click()

    time.sleep(2)
    driver1.get("http://steamcommunity.com/my/profile")
    time.sleep(0.2)
    element1 = driver1.find_element_by_xpath("/html/body/div[1]/div[7]/div[6]/div[1]/div[1]/div/div/div/div[3]/div[2]/a")
    element1.click()

first_account()
time.sleep(0.1)
second_account()

element = driver.find_element_by_xpath("/html/body/div[1]/div[7]/div[3]/div/div[2]/div/div/div[3]/div[2]/div[2]/form/div[3]/div[2]/div[3]/label/div[2]/input")
h = element.get_attribute("value")
element1 = driver1.find_element_by_xpath("/html/body/div[1]/div[7]/div[3]/div/div[2]/div/div/div[3]/div[2]/div[2]/form/div[3]/div[2]/div[3]/label/div[2]/input")
element.clear()
element1.clear()
element.send_keys(random_id)
element1.send_keys(h)
element = driver.find_element_by_xpath("/html/body/div[1]/div[7]/div[3]/div/div[2]/div/div/div[3]/div[2]/div[2]/form/div[7]/button[1]")
element1 = driver1.find_element_by_xpath("/html/body/div[1]/div[7]/div[3]/div/div[2]/div/div/div[3]/div[2]/div[2]/form/div[7]/button[1]")
element.click()
time.sleep(0.05)
element1.click()




