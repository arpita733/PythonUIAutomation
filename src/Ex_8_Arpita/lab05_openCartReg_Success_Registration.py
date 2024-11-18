import time

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.mark.positive
@allure.title("Positive Testcase - awesomeqa.com - Successful Registration")
@allure.description("Verify that if Privacy Policy Chcekbox in  checked, we will able to register")
def test_success_registration ( ) :
	driver = webdriver.Chrome()
	driver.get("https://awesomeqa.com/ui/index.php?route=account/register")
	first_Name = driver.find_element(By.XPATH, "//input[@id='input-firstname']")
	first_Name.send_keys("priya")
	last_name = driver.find_element(By.XPATH, "//input[@id='input-lastname']")
	last_name.send_keys("Mukherjee")
	email = driver.find_element(By.XPATH, "//input[@placeholder='E-Mail']")
	email.send_keys("aa@gmail.com")
	tele_ph = driver.find_element(By.XPATH, "//input[@id='input-telephone']")
	tele_ph.send_keys('9876543210')
	password = driver.find_element(By.XPATH, "//input[@id='input-password']")
	password.send_keys('Passowrd@123')
	conf_password = driver.find_element(By.XPATH, "//input[@id='input-confirm']")
	conf_password.send_keys('Passowrd@123')
	time.sleep(2)

	yes_radio_button = driver.find_element(By.XPATH,
										   "//input[@name='newsletter' and @value='1']")
	yes_radio_button.click()
	assert yes_radio_button.is_selected()
	check_privacy = driver.find_element(By.XPATH,
										"//input[@type='checkbox' and @name='agree' and @value='1']")

	if not check_privacy.is_selected() :
		check_privacy.click()
		assert check_privacy.is_selected()
	time.sleep(2)
	submit_registration = driver.find_element(By.XPATH,
											  "//input[@type='submit' and @value='Continue' and @class='btn btn-primary']")
	submit_registration.click()
	driver.get("https://awesomeqa.com/ui/index.php?route=account/success")
	success_message = driver.find_element(By.XPATH, "//h1[normalize-space(text())='Your Account Has Been Created!']")
	assert success_message.text == 'Your Account Has Been Created!'
	time.sleep(2)
	driver.quit()
# driver.back()
