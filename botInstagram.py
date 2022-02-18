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

def schearchOnInstagram(driver,manga):
    time.sleep(4)
    driver.get(f'https://www.instagram.com/explore/tags/{manga}/')
    time.sleep(4)
def goToAnAccount(account, driver):
    time.sleep(4)
    driver.get(f'https://www.instagram.com/{account}/')

def getFollowersOfAccount(driver, account, numberFollowers):
    goToAnAccount(account,driver)
    time.sleep(2)
    #getFollowersButton = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/div")
    getFollowersButton = driver.find_element_by_xpath("/html/body/div[1]/div/div/section/main/div/header/section/ul/li[2]/a/div")
    time.sleep(2)
    getFollowersButton.click()
    time.sleep(2)
    #Scroll down dans les abonnés
    pageFollowers = driver.find_element_by_xpath("/html/body/div[6]/div/div/div/div[2]")
    time.sleep(2)
    for _ in range(round((numberFollowers/10)+1)):
        driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", pageFollowers)
        time.sleep(1)
    #Permet de récupérer les abonnés
    time.sleep(4)
    count=0
    listFollowers=[]
    for i in range(1, numberFollowers+1):
        abo = driver.find_element_by_xpath("/html/body/div[6]/div/div/div/div[2]/ul/div/li["+str(i)+"]/div/div[1]/div[2]/div[1]/span/a/span").text
        print(abo)
        time.sleep(0.2)
        listFollowers.append(abo)
    return listFollowers   

#fonction pour s'abonner aux comptes
def sub(L,driver):
    for i in L:
        user=i
        time.sleep(1)
        driver.get(f'https://www.instagram.com/{user}/')
        time.sleep(3)
        try :
            alreadySubscribe = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[2]/div/span/span[1]/button/div/div/span")
            print("Déjà abonné à ce compte")
        except :
            try :
                isPrivate = driver.find_element_by_xpath("/html/body/div[1]/div/div/section/main/div/div/article/div[1]/div/h2")
                #subscribeButton = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div/button")
                subscribeButton = driver.find_element_by_xpath("/html/body/div[1]/div/div/section/main/div/header/section/div[1]/div[1]/div/div/button")
                subscribeButton.click
                print("Ce compte est en privé")
                time.sleep(0.5)
            except :
                #subscribeButton = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div/div/span/span[1]/button")
                subscribeButton = driver.find_element_by_xpath("/html/body/div[1]/div/div/section/main/div/header/section/div[1]/div[1]/div/div/div/span/span[1]/button")
                print("Ce compte est en public")
                time.sleep(0.5)
            subscribeButton.click()
            



driver = webdriver.Firefox(executable_path="geckodriver.exe")    
username = ""
username1 =""
username3=""
password = ""
driver = loginToInstagram(username3, password, driver)
account = "parisjetaime"
listFollowers = getFollowersOfAccount(driver, account, 400)
sub(listFollowers, driver)
#récupérer la taille d'un élément sizePageFollowers = pageFollowers.size['height']




