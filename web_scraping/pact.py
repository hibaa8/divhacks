from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json

color_dict = {
    "French Navy": "Blue",             # Remains "Blue"
    "Plum": "Purple",                  # Remains "Purple"
    "Baked Clay Bondi Stripe": "Red",  # Remains "Red"
    "Cornflower Bondi Stripe": "Blue",  # Remains "Blue"
    "Shadow": "Green",                 # Remains "Green"
    "Camel Bondi Stripe": "Yellow",    # Remains "Yellow"
    "Everyday Black Stripe": "Black",
    "Pomegranate Heather": "Red",
    "Sandshell Heather": "White",      # Remains "White"
    "French Navy Heather": "Blue",
    "Cinder": "Beige",                 # Changed to "Beige"
    "Olivine": "Green",                # Remains "Green"
    "Mahogany": "Brown",               # Remains "Brown"
    "Mountain View Meadow Floral": "Green",
    "Wheat Heather": "White",
    "Deep Taupe Heather": "Purple",
    "Charcoal Classic Stripe": "Black",
    "Mountain View": "Green",
    "Deep Taupe": "Purple",
    "Black": "Black",                  # No change
    "White": "White",
    "Ore": "Black",                    # Remains "Black"
    "Oat": "Beige",                    # Remains "Beige"
    "Festival Burst": "White",
    "Wharf Rat": "Gray",
    "Oat Heather": "Black",            # Remains "Black"
    "Sleeping Vines": "Green",
    "Berry Sprigs": "Red",
    "Soft Flutters": "Pink",
    "Sleeping In": "Black",
    "Mauve": "Red",
    "Butter": "White",
    "Harvest Hues": "Orange",
    "Floral": "Yellow",
    "Chalk Pink": "Pink",
    "Ink Blue": "Blue",
    "Carob": "Brown",
    "Vineyard": "Red",
    "Brisk Blues": "Blue",
    "Frosty Green": "Green",
    "Harvest Moon": "Orange",
    "Autumn Hues": "Brown",
    "Deep Taupe": "Purple",
    "Deep Taupe Heather": "Purple",
    "Dark Forest": "Green",             # Changed to "Green"
    "Heather Grey": "Gray",
    "Orchid Petal": "Purple",
    "Black": "Black",
    "Charcoal Heather": "Gray",         # Remains "Gray"
    "Blue Bells": "Blue",               # Changed to "Blue"
    "Mountain View": "Green",
    "Sesame": "Beige",                  # Changed to "Beige"
    "Storm": "Black",                   # Changed to "Black"
    "Cayenne": "Red",                   # Remains "Red"
    "Wedgewood": "Blue",                # Remains "Blue"
    "Jade": "Green"                     # Remains "Green"
}

type_dict = {
    't-shirt': 'Tops',
    'tank top': 'Tops',
    'blouse': 'Tops',
    'shirt': 'Tops',
    'sweater': 'Sweaters',
    'sweatshirt': 'Sweaters',
    'polo shirt': 'Tops',
    'camisole': 'Tops',
    'crop top': 'Tops',
    'bodysuit': 'Tops',
    'henley': 'Tops',
    'rugby shirt': 'Tops',
    'graphic tee': 'Tops',
    'long-sleeve shirt': 'Tops',
    'jacket': 'Jackets',
    'blazer': 'Jackets',
    'coat': 'Jackets',
    'cardigan': 'Sweaters',
    'vest': 'Jackets',
    'poncho': 'Other',
    'raincoat': 'Jackets',
    'windbreaker': 'Jackets',
    'anorak': 'Jackets',
    'duster': 'Jackets',
    'kimono': 'Other',
    'cape': 'Other',
    'shrug': 'Other',
    'jean': 'Pants',
    'trouser': 'Pants',
    'legging': 'Pants',
    'short': 'Pants',
    'skirt': 'Other',
    'jogger': 'Pants',
    'sweatpant': 'Pants',
    'overall': 'Pants',
    'culotte': 'Pants',
    'capri': 'Pants',
    'cargo pant': 'Pants',
    'palazzo pant': 'Pants',
    'track pant': 'Pants',
    'jumpsuit/romper': 'Other',
    'sheath dress': 'Other',
    'a-line dress': 'Other',
    'wrap dress': 'Other',
    'maxi dress': 'Other',
    'midi dress': 'Other',
    'mini dress': 'Other',
    'shirt dress': 'Other',
    'bodycon dress': 'Other',
    'fit-and-flare dress': 'Other',
    'empire waist dress': 'Other',
    'shift dress': 'Other',
    'kaftan': 'Other',
    'tunic dress': 'Other',
    'sun dress': 'Other',
    'evening gown': 'Other',
    'cocktail dress': 'Other',
    'slip dress': 'Other',
    'off-shoulder dress': 'Other',
    'sweater dress': 'Sweaters',
    'bra': 'Other',
    'underwear': 'Other',
    'slip': 'Other',
    'pantyhose': 'Other',
    'tight': 'Other',
    'sock': 'Other',
    'lingerie': 'Other',
    'shapewear': 'Other',
    'thermal underwear': 'Other',
    'nightgown': 'Other',
    'pajama': 'Other',
    'robe': 'Other',
    'sleep shirt': 'Tops',
    'onesie': 'Other',
    'sports bra': 'Other',
    'compression top': 'Tops',
    'compression short': 'Pants',
    'yoga pant': 'Pants',
    'track jacket': 'Jackets',
    'sweat-wicking shirt': 'Tops',
    'sports jersey': 'Tops',
    'gym short': 'Pants',
    'rash guard': 'Tops',
    'base layer': 'Other',
    'dress shirt': 'Tops',
    'dress pant': 'Pants',
    'pencil skirt': 'Other',
    'suit': 'Jackets',
    'chino': 'Pants',
    'dress top': 'Tops',
    'formal shirt': 'Tops',
    'tuxedo': 'Jackets',
    'ball gown': 'Other',
    'tailcoat': 'Jackets',
    'waistcoat': 'Jackets',
    'sari': 'Other',
    'hanbok': 'Other',
    'kurta': 'Other',
    'dashiki': 'Other',
    'dirndl': 'Other',
    'lehenga': 'Other',
    'abaya': 'Other',
    'kebaya': 'Other',
    'cheongsam (qipao)': 'Other',
    'sarong': 'Other',
    'one-piece swimsuit': 'Other',
    'bikini': 'Other',
    'swim trunk': 'Pants',
    'board short': 'Pants',
    'cover-up': 'Other',
    'swim dress': 'Other',
    'tankini': 'Other',
    'belt': 'Other',
    'scarf': 'Other',
    'hat': 'Other',
    'glove': 'Other',
    'mitten': 'Other',
    'sunglass': 'Other',
    'bandana': 'Other',
    'tie': 'Other',
    'bow tie': 'Other',
    'suspender': 'Other',
    'handkerchief': 'Other',
    'face mask': 'Other',
    'T-shirts': 'Tops',
    'Tank tops': 'Tops',
    'Blouses': 'Tops',
    'Shirts': 'Tops',
    'Sweaters': 'Sweaters',
    'Sweatshirts': 'Sweaters',
    'Polo shirts': 'Tops',
    'Camisoles': 'Tops',
    'Crop tops': 'Tops',
    'Bodysuits': 'Tops',
    'Henleys': 'Tops',
    'Rugby shirts': 'Tops',
    'Graphic tees': 'Tops',
    'Long-sleeve shirts': 'Tops',
    'Jackets': 'Jackets',
    'Blazers': 'Jackets',
    'Coats': 'Jackets',
    'Cardigans': 'Sweaters',
    'Vests': 'Jackets',
    'Ponchos': 'Other',
    'Raincoats': 'Jackets',
    'Windbreakers': 'Jackets',
    'Anoraks': 'Jackets',
    'Dusters': 'Jackets',
    'Kimonos': 'Other',
    'Capes': 'Other',
    'Shrugs': 'Other',
    'Jeans': 'Pants',
    'Trousers': 'Pants',
    'Leggings': 'Pants',
    'Shorts': 'Pants',
    'Skirts': 'Other',
    'Joggers': 'Pants',
    'Sweatpants': 'Pants',
    'Overalls': 'Pants',
    'Culottes': 'Pants',
    'Capris': 'Pants',
    'Cargo pants': 'Pants',
    'Palazzo pants': 'Pants',
    'Track pants': 'Pants',
    'Jumpsuits/Rompers': 'Other',
    'Sheath dresses': 'Other',
    'A-line dresses': 'Other',
    'Wrap dresses': 'Other',
    'Maxi dresses': 'Other',
    'Midi dresses': 'Other',
    'Mini dresses': 'Other',
    'Shirt dresses': 'Other',
    'Bodycon dresses': 'Other',
    'Fit-and-flare dresses': 'Other',
    'Empire waist dresses': 'Other',
    'Shift dresses': 'Other',
    'Kaftans': 'Other',
    'Tunic dresses': 'Other',
    'Sun dresses': 'Other',
    'Evening gowns': 'Other',
    'Cocktail dresses': 'Other',
    'Slip dresses': 'Other',
    'Off-shoulder dresses': 'Other',
    'Sweater dresses': 'Sweaters',
    'Bras': 'Other',
    'Underwear': 'Other',
    'Slips': 'Other',
    'Pantyhose': 'Other',
    'Tights': 'Other',
    'Socks': 'Other',
    'Lingerie': 'Other',
    'Shapewear': 'Other',
    'Thermal underwear': 'Other',
    'Nightgowns': 'Other',
    'Pajamas': 'Other',
    'Robes': 'Other',
    'Sleep shirts': 'Tops',
    'Onesies': 'Other',
    'Sports bras': 'Other',
    'Compression tops': 'Tops',
    'Compression shorts': 'Pants',
    'Yoga pants': 'Pants',
    'Track jackets': 'Jackets',
    'Sweat-wicking shirts': 'Tops',
    'Sports jerseys': 'Tops',
    'Gym shorts': 'Pants',
    'Rash guards': 'Tops',
    'Base layers': 'Other',
    'Dress shirts': 'Tops',
    'Dress pants': 'Pants',
    'Pencil skirts': 'Other',
    'Suits': 'Jackets',
    'Chinos': 'Pants',
    'Dress tops': 'Tops',
    'Formal shirts': 'Tops',
    'Tuxedos': 'Jackets',
    'Ball gowns': 'Other',
    'Tailcoats': 'Jackets',
    'Waistcoats': 'Jackets',
    'Saris': 'Other',
    'Hanboks': 'Other',
    'Kurtas': 'Other',
    'Dashikis': 'Other',
    'Dirndls': 'Other',
    'Lehengas': 'Other',
    'Abayas': 'Other',
    'Kebayas': 'Other',
    'Cheongsams (Qipaos)': 'Other',
    'Sarongs': 'Other',
    'One-piece swimsuits': 'Other',
    'Bikinis': 'Other',
    'Swim trunks': 'Pants',
    'Board shorts': 'Pants',
    'Cover-ups': 'Other',
    'Swim dresses': 'Other',
    'Tankinis': 'Other',
    'Belts': 'Other',
    'Scarves': 'Other',
    'Hats': 'Other',
    'Gloves': 'Other',
    'Mittens': 'Other',
    'Sunglasses': 'Other',
    'Bandanas': 'Other',
    'Ties': 'Other',
    'Bow ties': 'Other',
    'Suspenders': 'Other',
    'Handkerchiefs': 'Other',
    'Face masks': 'Other'
}

def getProductData(url):
    product_list = []
    driver = webdriver.Chrome()
    driver.get(url)

    product_links = []
    one_product_el = driver.find_elements(By.CSS_SELECTOR, ".pactV1-xshop-card")

    for product in one_product_el:
        try:
            link_element = product.find_element(By.TAG_NAME, 'a')
            product_link = link_element.get_attribute('href')
            product_links.append(product_link)
        except Exception as e:
            print(f"Error while extracting link: {e}")

    for product_link in product_links:
        try:
            val={}
            driver.get(product_link)
            
            # Wait for the product details to be present on the new page
            product_details = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".product-details"))  # Adjust the selector for details
            )

            images = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "product-images-slides-desktop-wrapper"))  # Adjust the selector for details
            )
            
            # Extract the desired data from the product details
            # product_details_ul = product_details.find_element(By.CSS_SELECTOR, ".product-information-care ul")
            product_details_el = "95% Organic Cotton" #most products are 95%, very few are 75%, 97%, and 100%. sorry for hardcoding had to cut corners for sake of time
            price_el = product_details.find_element(By.CSS_SELECTOR, ".dollar").text
            description_el_raw = product_details.find_element(By.CSS_SELECTOR, ".product-details-display-features").text
            description_el = description_el_raw.replace('\n', ' ')  
            brand_el = "Pact"
            color_el_weird = product_details.find_element(By.CSS_SELECTOR, ".product-color-name").text
            all_words = description_el.split()

            type_el = ""

            for i in all_words:
                if i.lower() in type_dict:
                    type_el = type_dict[i]
                    break
            
            if type_el == "":
                type_el = "Other"

            if color_el_weird in color_dict:
                color_el = color_dict[color_el_weird]
            else:
                color_el = "Black"

            image_el = images.find_element(By.CSS_SELECTOR, ".product-images img:first-of-type")
            image_link = image_el.get_attribute('src')

            val["product_details"] = product_details_el #materials
            val["price"] = price_el
            val["description"] = description_el
            val["brand"] = brand_el
            val["color"] = color_el
            val["url"] = product_link
            val["image"] = image_link
            val["type"] = type_el

            product_list.append(val)

        except Exception as e:
            print(f"Error while scraping product {product_link}: {e}")

    driver.close()

    return product_list

#data1 = getProductData("https://wearpact.com/women/apparel")
#data2 = getProductData("https://wearpact.com/women/clearance")
data3 = getProductData("https://wearpact.com/women/new")

with open("data.jsonl", "a") as f:
    for entry in data3:
        json.dump(entry, f)
        f.write('\n')