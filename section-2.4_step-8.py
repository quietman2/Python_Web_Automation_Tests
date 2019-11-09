from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    price = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"),"100")
    )

    button = WebDriverWait(browser, 15).until(
        EC.element_to_be_clickable((By.ID, "book"))
    )

    button.click()

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    input_field = browser.find_element_by_id("answer").send_keys(y)

    submit_button = browser.find_element_by_id("solve")
    submit_button.click()


finally:
    time.sleep(10)

    browser.quit()