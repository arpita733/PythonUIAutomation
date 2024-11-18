import time

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.mark.Negative
@allure.title("Negative Testcase - awesomeqa.com - Mandatory checkbox unselected -> Warning Message.")
@allure.description("Verify that if Privacy Policy Chcekbox in not checked, we will get a warning")
def test_Open_Cart_Registration ( ) :
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
	time.sleep(5)

	submit_registration = driver.find_element(By.XPATH,
											  "//input[@type='submit' and @value='Continue' and @class='btn btn-primary']")

	print(submit_registration.text)
	submit_registration.click()

	error_message = driver.find_element(By.XPATH,
									"//div[@class='alert alert-danger alert-dismissible' and normalize-space(text())='Warning: You must agree to the Privacy Policy!']")
	#Why normalize-space?It trims any unnecessary whitespace, ensuring the text content matches precisely, which is particularly useful when the message is formatted across multiple lines or includes spaces.
	print(error_message.text)
# error_message = driver.find_element(By.XPATH,"//div[@class='alert alert-danger alert-dismissible' and contains('Warning: You must agree to the Privacy Policy!')]")

	assert error_message.text == 'Warning: You must agree to the Privacy Policy!'
	driver.implicitly_wait(5)
