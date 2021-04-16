import sys
sys.tracebacklimit=0

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.mcdfoodforthoughts.com")

next = driver.find_element_by_xpath('//*[@id="NextButton"]')
next.click()

try:
    element = WebDriverWait(driver, 10). until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[3]/div[2]/form/div/div[1]/div[2]/div[1]/span/span"))
    )
    element.click()
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "NextButton"))
    )
    element.click()
    CN1 = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/form/div/p[2]/span[2]/input[1]")
    CN2 = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/form/div/p[2]/span[2]/input[2]")
    CN3 = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/form/div/p[2]/span[2]/input[3]")

###############################
    CN1.send_keys("CF4C")
    CN2.send_keys("QZNY")
    CN3.send_keys("XFF4")
###############################

    Pound = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/form/div/p[3]/span[2]/input[1]")
    Pence = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/form/div/p[3]/span[2]/input[2]")
    Pound.send_keys("5")
    Pence.send_keys("99")
    while True:
        try:
            element = WebDriverWait(driver, 2).until(
                EC.presence_of_element_located((By.ID, "NextButton"))
            )
            element.click()
            continue
        except:
            break
finally:
    print("cheap burger baby xd !!!!!!!!!!!!!!!!!!!!")
    code = driver.find_elements_by_class_name("ValCode")[0].text
    print("------>" + code + "<------")
    driver.close()

# to use 1) change input mcdonalds reciept code into CN1/2/3 2) then click run for burger
