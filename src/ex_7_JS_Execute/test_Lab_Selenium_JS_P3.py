import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains, ActionBuilder
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.mouse_button import MouseButton


@allure.title("JS")
@allure.description("Verify JS")
def test_js():
    # ChromeOptions - --incognito
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")

    driver = webdriver.Chrome(chrome_options)
    driver.get("https://selectorshub.com/xpath-practice-page/")
    driver.maximize_window()
    # Synchronously Executes JavaScript in the current window/frame.

    # This title we are finding via the JS code.
    title = driver.execute_script("return document.title")

    #driver.current_url  - Webdriver finding the url via the API request.



    current_url = driver.execute_script("return document.URL")

    print(current_url)
    print(title)



    time.sleep(5)
    driver.quit()
