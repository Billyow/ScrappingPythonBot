from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys
service = Service("X:/Usuario/Escritorio/Trabajos/Proyecto de construccion de SW/parcticas_python/chromedriver-win64/chromedriver.exe")


bot= webdriver.Chrome(service=service)
bot.get("https://www.exito.com/")
sleep(1)
bot.maximize_window()
#find the cookies accept btn and accept them
cookies = bot.find_element(By.XPATH,'/html/body/div[1]/section/div/button')
cookies.click()
#find the input to make the search
inputBtn = bot.find_element(By.XPATH,'//*[@id="header-page"]/section/div/div[1]/div[2]/form/input')
sleep(1)
inputBtn.click()
sleep(1)
search = "celulares Iphone"
#type the search in the input
inputBtn.send_keys(search)
sleep(1)
#type enter to make the search
inputBtn.send_keys(Keys.ENTER)
sleep(5)
#find the sold by filter and click it
soldByFilter = bot.find_element(By.XPATH,'/html/body/div/main/section[3]/div/div[1]/div[1]/div/div/div[8]/button')
sleep(1)
#scroll to the sold by filter to make it visible
bot.execute_script("arguments[0].scrollIntoView(true);", soldByFilter)
soldByFilter.click()
sleep(1)
#find the checkbox for Exito in the sold by filter and click it
exitoCheckbox = bot.find_element(By.XPATH,'/html/body/div/main/section[3]/div/div[1]/div[1]/div/div/div[8]/div/ul/li[1]/input')
sleep(1)
exitoCheckbox.click()
sleep(1)
#find the apply filter button and click it
applyFilter = bot.find_element(By.XPATH,'/html/body/div/main/section[3]/div/div[1]/div[2]/button')
sleep(1)
applyFilter.click()
sleep(6)

def listAllPhones(path):
    products = []
    productsList = bot.find_elements(By.XPATH, path)
    for li in productsList:
        try:
            name = li.find_element(By.XPATH, './/article/div[1]/div[2]/a/h3').text
            price = li.find_element(By.XPATH, '..//article/div[1]/div[2]/div/div/div[2]/p[1]').text
            
            products.append({
                "name": name,
                "price": price,
            })
        except:
            continue
    return products
sleep(2)
firstPagePhones = listAllPhones('/html/body/div[1]/main/section[3]/div/div[2]/div[2]/div[2]/ul/li')
#find the second page button
secondPage = bot.find_element(By.XPATH,'/html/body/div[1]/main/section[3]/div/div[2]/div[2]/div[3]/section/div/ul/li[2]/button')
#scroll to the second page button to make it visible
bot.execute_script("arguments[0].scrollIntoView(true);", secondPage)
sleep(2)
#click the second page button
secondPage.click()
sleep(6)
#find the products list again in the second page
secondPagePhones=listAllPhones('/html/body/div[1]/main/section[3]/div/div[2]/div[2]/div[2]/ul/li')

allPhones=firstPagePhones+secondPagePhones

#convert to json
import json
with open('X:/Usuario/Escritorio/Trabajos/Proyecto de construccion de SW/parcticas_python/json/products.json', 'w') as f:
    json.dump(allPhones, f, indent=4)

footer = bot.find_element(By.XPATH,'/html/body/div[1]/footer/section[3]/div/div[1]/button')
bot.execute_script("arguments[0].scrollIntoView(true);", footer)
sleep(1)
footer.click()
sleep(1)

bot.save_screenshot('X:/Usuario/Escritorio/Trabajos/Proyecto de construccion de SW/parcticas_python/img/salesBtn.png')
sleep(2)
# close the browser 
bot.quit()

