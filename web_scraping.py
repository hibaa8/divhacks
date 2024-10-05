from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

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

print(getProductData("https://www.amazon.com/XIUYANG-Womens-Smiling-Embroidery-colour/dp/B0CY1KFRZ4/ref=sxin_16_pa_sp_search_thematic_sspa?content-id=amzn1.sym.75c2cce7-1de2-485e-ad57-5eb3abc42d20%3Aamzn1.sym.75c2cce7-1de2-485e-ad57-5eb3abc42d20&crid=KF09WQFT867P&cv_ct_cx=socks+for+women+blue+black+and+grey+christmas+diagonal+treehouse+radio&dib=eyJ2IjoiMSJ9.CseozB77r_e3JsEbYnj6C0ycgrDBLCzs1oXfkhgb9AAc_7VuBYaR2pcNyELaDFNvVmdLpDJZoeaBvZTfiCw1ew.PjKqjSflpu-5OBzsW-rw2WWeRlcAQEKtFwmwA16qfuM&dib_tag=se&keywords=socks+for+women+blue+black+and+grey+christmas+diagonal+treehouse+radio&pd_rd_i=B0CY1KFRZ4&pd_rd_r=12a42ba0-3b85-4bd3-93cb-0d9f6bafaee0&pd_rd_w=fTqPy&pd_rd_wg=7cWPZ&pf_rd_p=75c2cce7-1de2-485e-ad57-5eb3abc42d20&pf_rd_r=WVHY99R9KNQ69VZ965XT&qid=1728156452&sbo=RZvfv%2F%2FHxDF%2BO5021pAnSA%3D%3D&sprefix=%2Caps%2C290&sr=1-4-183302c6-8dec-4386-8e58-6031e7be5ad8-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9zZWFyY2hfdGhlbWF0aWM&psc=1"))