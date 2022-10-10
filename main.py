from hashlib import new
from lib2to3.pgen2.driver import Driver
from tkinter import Variable
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import time

#OUR INFO

Name=["Dimitrios K"]
Email=["example@email.com"]
Tel=["6912345678"]
Address=["CityStreet 1"]
City=["Athens"]
TXK=["12345"]
CardInfo=["5167000000000000"]
CCC=["123"]


#THE COLOR Variable
ProductColor="Tan"
#THE PRODUCT VARIBLE
ProductCat="HoodeDd"

#OPENING THE SITE
driver = webdriver.Firefox()
driver.get("https://www.supremenewyork.com/shop/all/jackets")

time.sleep(1)

#THE "CONTAINER" CONTAINS THE NUMBER OF PRODUCTS 
ProductList=driver.find_elements(By.XPATH, '//*[@id="container"]/*')

#IF THE PRODUCT  HAS THE TEXT WE HAVE SPECIFIED IT WILL BE SELECTED ,ELSE WE REFRESH THE PAGE
found=False  
while 1:
    MinValue=0
    for i in ProductList:
        try:
            if driver.find_element(By.XPATH, f"//article[{MinValue}]/div/h1/a[contains(text(),'{ProductCat}')]") and driver.find_element(By.XPATH, f"//article[{MinValue}]/div/p/a[contains(text(),'{ProductColor}')]"):
                driver.find_element(By.XPATH, f"//article[{MinValue}]").click()
                found=True
                break   
        except NoSuchElementException:
            MinValue +=1
    if found==True:
        break
    driver.refresh()
    
#GET THE PRODUCT IN THE CART
time.sleep(1)
driver.find_element(By.CSS_SELECTOR ,"input.button").click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR ,"a.button:nth-child(3)").click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR , "div.icheckbox_minimal:nth-child(2) > ins:nth-child(2)").click()


#FILL THE PURCHASE FORM WITH OUR INFO

FormName=driver.find_element(By.XPATH , '//*[@id="order_billing_name"]')
FormName.send_keys(Name)

FormMail=driver.find_element(By.XPATH , '//*[@id="order_email"]')
FormMail.send_keys(Email) 

FormTel=driver.find_element(By.XPATH , '//*[@id="order_tel"]')
FormTel.send_keys(Tel) 

FormAdress=driver.find_element(By.XPATH , '//*[@id="order_billing_address"]')
FormAdress.send_keys(Address)

FormCity=driver.find_element(By.XPATH , '//*[@id="order_billing_city"]')
FormCity.send_keys(City)

FormTXK=driver.find_element(By.XPATH , '//*[@id="order_billing_zip"]')
FormTXK.send_keys(City)

FormCardInfo=driver.find_element(By.XPATH , '//*[@id="credit_card_number"]')
FormCardInfo.send_keys(CardInfo)

FormCCC=driver.find_element(By.XPATH , '//*[@id="credit_card_verification_value"]')
FormCCC.send_keys(CCC)

select = Select(driver.find_element(By.XPATH , '//*[@id="order_billing_country"]'))
select.select_by_visible_text("GREECE")

INPUT=input("Closing this will also close the browser")

