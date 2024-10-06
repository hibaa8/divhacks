from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def getProductData(url):
    val={}
    driver = webdriver.Chrome()
    driver.get(url)
    product_details_el = driver.find_element(By.ID, "productFactsDesktop_feature_div")
    price_el = driver.find_element(By.ID, "corePriceDisplay_desktop_feature_div")
    description_el = driver.find_element(By.ID, "title_feature_div")
    brand_el = driver.find_element(By.ID, "bylineInfo_feature_div")

    val["product_details"] = product_details_el.text
    val["price"] = price_el.text
    val["description"] = description_el.text
    val["brand"] = brand_el.text

    driver.close()

    return val

print(getProductData(""))