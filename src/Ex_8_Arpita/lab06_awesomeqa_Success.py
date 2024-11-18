import time

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import *
from selenium.webdriver.support.ui import Select


@pytest.mark.positive
@allure.title("Positive Testcase - awesomeqa.com - Successful Registration")
@allure.description("Verify that if Privacy Policy Chcekbox in  checked, we will able to register")
def test_validate_elements ( ) :
	driver = webdriver.Chrome()
	driver.get("https://awesomeqa.com/practice.html")
	first_Name = driver.find_element(By.XPATH, "//input[@name='firstname' and @type='text']")
	first_Name.send_keys("priya")
	time.sleep(2)
	last_name = driver.find_element(By.XPATH, "//input[@name='lastname' and @type='text']")
	last_name.send_keys("Mukherjee")
	time.sleep(2)
	gender_radio_button = driver.find_element(By.XPATH,
											  "//input[@id='sex-1' and @value='Female']")
	gender_radio_button.click()
	time.sleep(2)
	assert gender_radio_button.is_selected()

	Year_ofExp_radio_button = driver.find_element(By.XPATH,
												  "//input[@id='exp-5' and @type='radio' and @value='6']")

	Year_ofExp_radio_button.click()
	assert Year_ofExp_radio_button.is_selected()

	Date_input = driver.find_element(By.XPATH, "//input[@id='datepicker' and @type='text']")
	Date_input.send_keys("18/11/2024")
	time.sleep(2)
	profession_checkbox = driver.find_element(By.XPATH,
											  "//input[@id='profession-1' and @type='checkbox' and @value='Automation Tester']")
	if not profession_checkbox.is_selected() :
		profession_checkbox.click()
	time.sleep(5)

	tool_checkbox = driver.find_element(By.XPATH,
										"//input[@id='tool-2' and @type='checkbox' and @value='Selenium Webdriver']")
	if not tool_checkbox.is_selected() :
		tool_checkbox.click()
	time.sleep(5)

	multiselect_dd = driver.find_element(By.XPATH, "//select[@name='continents' and @class='input-xlarge']")
	select = Select(multiselect_dd)
	select.select_by_visible_text('Asia')
	select.select_by_visible_text('Australia')
	time.sleep(5)
	command_dropdown = driver.find_element(By.XPATH, "//select[ @class ='input-xlarge' and @ name='selenium_commands']")
	select_new = Select(command_dropdown)
	select_new.select_by_index(2)
	select_new.select_by_index(4)
	time.sleep(5)

	file_upload = driver.find_element(By.XPATH, "//input[@class='input-file' and @id='photo' and @type='file']")
	file_path = r'D:\class 9\beng\PROJ\mulayon.jpg'  # The r prefix ensures the string is treated as-is, without interpreting any escape sequences, making it especially useful for file paths or regular expressions.
	file_upload.send_keys(file_path)

	time.sleep(3)

	driver.quit()
