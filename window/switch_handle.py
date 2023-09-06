from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import math

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
driver = webdriver.Chrome(options=chrome_options)

link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/redirect_accept.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    driver.get(link2)
    driver.set_window_size(1500, 1000)

    start_button = driver.find_element(By.XPATH, "/html/body/form/div/div/button")
    start_button.click()

    new_window = driver.window_handles[1]
    driver.switch_to.window(new_window)

    text1 = driver.find_element(By.CSS_SELECTOR, "[id = 'input_value']")
    x = text1.text
    print(x)
    input1 = driver.find_element(By.CSS_SELECTOR, "[id = 'answer']")
    y = calc(x)
    input1.send_keys(y)
    print(y)

    button = driver.find_element(By.XPATH, "/html/body/form/div/div/button")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    driver.quit()