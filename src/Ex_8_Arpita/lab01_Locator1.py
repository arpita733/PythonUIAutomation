import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


#@pytest.mark.skip
@pytest.mark.negative
@allure.title("Negative Testcase - App.vwo.com - Wrong Email, Pass -> Error Message.")
@allure.description("Verify that if email/pass is wrong, we will get a message")
def test_email_verification ( ) :
	driver = webdriver.Chrome()
	driver.get("https://app.vwo.com/#/login")
	email_element = driver.find_element(By.ID, "login-username")
	email_element.send_keys("arpitamukherjee517@gmail.com")
	pw_element = driver.find_element(By.NAME, "password")
	pw_element.send_keys("Aishani@2011")
	# remember = driver.find_element(By.ID, value="checkbox-remember")
	# remember.click()
	# assert remember.is_selected()
	signin_btn = driver.find_element(By.ID, "js-login-btn")
	signin_btn.click()

	WebDriverWait(driver=driver, timeout=5).until(EC.visibility_of_element_located((By.CLASS_NAME, "notification-box-description")))

	error_message = driver.find_element(By.CLASS_NAME, "notification-box-description")
	assert error_message.text == "Your email, password, IP address or location did not match"

	driver.quit()


def test_link ( ) :
	driver = webdriver.Chrome()
	driver.get("https://app.vwo.com/#/login")
	click_link = driver.find_element(By.LINK_TEXT, "Start a free trial")
	click_link.click()
	assert driver.current_url == "https://vwo.com/free-trial/?utm_medium=website&utm_source=login-page&utm_campaign=mof_eg_loginpage"


def test_count_of_link_in_screen ( ) :
	driver = webdriver.Chrome()
	driver.get("https://app.vwo.com/#/login")
	link_component = driver.find_elements(By.TAG_NAME, "a")
	print(len(link_component))
	for i in link_component :
		print(i.text)


def test_count_of_buttons_in_screen ( ) :
	driver = webdriver.Chrome()
	driver.get("https://app.vwo.com/#/login")
	button_component = driver.find_elements(By.TAG_NAME, "button")
	print(len(button_component))
	for i in button_component :
		print(i.text)
