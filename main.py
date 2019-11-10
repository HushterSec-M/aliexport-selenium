from selenium import webdriver
from time import sleep

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
def auth():
    driver.get("https://ru.aliexpress.com")
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "html")))
    try:
        element = driver.find_element_by_css_selector('.close-layer')
        element.click()
        sleep(3)
    except:
        pass
    element = driver.find_element_by_id("nav-user-account")
    element.click()
    sleep(1)
    element = driver.find_element_by_class_name("sign-btn")
    element.click()
    sleep(2)
    WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.ID, "alibaba-login-box")))
    sleep(1)
    element = driver.find_element_by_id("fm-login-id")
    element.send_keys("") #login
    element = driver.find_element_by_id("fm-login-password")
    element.send_keys("") #password
    sleep(2)
    element = driver.find_element_by_class_name("fm-btn")
    element.click()
    sleep(3)


def create_list(url):
    driver.get(url)
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "html")))
    while 1:
        elements = driver.find_elements_by_class_name("product-item")
        sleep(1)
        llen = len(elements)
        driver.find_element(By.XPATH, '//a[@data-role="viewmore"]').click()
        sleep(2)
        elements = driver.find_elements_by_class_name("product-item")
        flen = len(elements)
        if llen==flen: break
    elems = driver.find_elements_by_xpath("//a[@href]")
    doelems = []
    for elem in elems:
        attr = elem.get_attribute("href")
        if (attr.startswith("https://www.aliexpress.com/item/") and (attr not in doelems)):
            print(f"add to dolist: {attr}")
            doelems.append(attr)
    print(len(doelems))
        #else:
        #    print("         " + attr)
    return doelems
def add(item):
    driver.get(item)
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "html")))
    sleep(2)
    button = driver.find_element_by_class_name("add-wishlist-wrap")
    if button: print("button find: ", end="")
    sleep(1)
    button.click()



if __name__ == "__main__":
    auth()
    url_collections = [
        "https://s.click.aliexpress.com/e/2FWgC1c",
        #"https://s.click.aliexpress.com/e/chpolU8i",
    ]
    i = 0
    for url in url_collections:
        list = create_list(url)
        for item in list:
            i+=1
            try:
                add(item)
                print(f"    do: {item} : {i}")
                sleep(2)
            except:
                print(f"error: {item} : {i}")
                continue
1
Downloading1