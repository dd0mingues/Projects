from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

def sellDupes():
    connection_url = 'https://www.urban-rivals.com/collection/'

    driver = webdriver.Firefox()
    driver.get(connection_url)

    wait = WebDriverWait(driver, 100)

    time.sleep(3)

    cookies_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "js-urmodal-validate")))
    cookies_button.click()

    select = Select(wait.until(EC.presence_of_element_located((By.NAME, "group"))))
    select.select_by_value('double')

    select = Select(wait.until(EC.presence_of_element_located((By.NAME, "sortby"))))
    select.select_by_value('level')

    select = Select(wait.until(EC.presence_of_element_located((By.NAME, "orderby"))))
    select.select_by_value('desc')

    while True:
        try:
            sell_button =  wait.until(EC.presence_of_element_located((By.CLASS_NAME, "btn-sell-card")))
            sell_button.click()

            sell_price = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "form-text"))).text.split('minimum price: ')[1].split(' C')[0]
            input_field = wait.until(EC.presence_of_element_located((By.ID, "form-sellprice")))

            input_field.send_keys(sell_price)

            buttons_on_screen = wait.until(EC.presence_of_all_elements_located ((By.CLASS_NAME, "btn-ur")))
            buttons_on_screen[4].click()
        except:
            False

