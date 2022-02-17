from lib2to3.pgen2 import driver
from multiprocessing import managers
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

def loginToInstagram(username, password, driver):
    driver.get("https://www.instagram.com/")
    time.sleep(2)
    cookie_button = driver.find_element_by_xpath("//button[text()='Accepter tout']")
    cookie_button.click()
    time.sleep(3)
    getUsername = driver.find_element_by_name("username")
    getUsername.send_keys(username)
    time.sleep(1)
    getPassword = driver.find_element_by_name("password")
    getPassword.send_keys(password)
    time.sleep(2)
    getPassword.send_keys(Keys.ENTER)
    time.sleep(4)
    return driver

def schearchOnInstagram(driver,manga) :
    time.sleep(4)
    driver.get("https://www.instagram.com/explore/tags/"+manga+"/")
    time.sleep(4)

def getFollowersOfAccount(driver, account, numberFollowers) :
    time.sleep(4)
    driver.get("https://www.instagram.com/"+account+"/")
    time.sleep(2)
    getFollowersButton = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/div")
    time.sleep(2)
    getFollowersButton.click()
    time.sleep(2)
    #Scroll down dans les abonnés
    pageFollowers = driver.find_element_by_xpath("/html/body/div[6]/div/div/div/div[2]")
    time.sleep(2)
    for j in range(round(numberFollowers/10)) :
        driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", pageFollowers)
        time.sleep(1)
    #Permet de récupérer les abonnés
    time.sleep(4)
    count=0
    for i in range(1,numberFollowers+1,1) :
        abo = driver.find_element_by_xpath("/html/body/div[6]/div/div/div/div[2]/ul/div/li["+str(i)+"]/div/div[1]/div[2]/div[1]/span/a/span").text
        print(abo)
        time.sleep(0.2)
        count=count+1
        print(count)    



driver = webdriver.Firefox(executable_path="geckodriver.exe")    
username = "comptewish10nicolas@gmail.com"
username1 ="lalaya3137@bepureme.com"
password = "BgDu02600123"
driver = loginToInstagram(username, password, driver)
account = "nicodrain"
getFollowersOfAccount(driver, account, 179)
#récupérer la taille d'un élément sizePageFollowers = pageFollowers.size['height']
