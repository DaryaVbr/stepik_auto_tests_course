from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

def calc(x):
    return str(math.log(abs(12*math.sin(x))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    button = browser.find_element(By.ID, 'book')
    image = WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), '$100')
        )
    button.click()

    button_2 = browser.find_element(By.ID, 'solve')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button_2)

    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(int(x))

    input_1 = browser.find_element(By.ID, 'answer')
    input_1.send_keys(y)

    button_2.click()

    wind_alert = browser.switch_to.alert
    mess = wind_alert.text
    print(mess)

finally:
    browser.quit()