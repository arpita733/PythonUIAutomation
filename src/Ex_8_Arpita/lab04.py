# Task details
# Open the Url - https://www.ebay.com/b/Desktops-All-In-One-Computers/171957/bn_1643067
# Search for the Macmini
# Click on the search ICON
# Get all the titles
# Get al the prices
# Print all the titles and prices in the end

import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_xpath_container_title_price ( ) :
	# Set up Chrome WebDriver
	global list_of_items_price, list_of_items
	driver1 = webdriver.Edge()
	driver1.maximize_window()
	driver1.get("https://www.ebay.com/b/Desktops-All-In-One-Computers/171957/bn_1643067")

	time.sleep(3)  # search_box_element=driver1.find_element(By.XPATH, "//input[@id='gh-ac']")
	search_box_element = driver1.find_element(By.XPATH, "//input[@placeholder = 'Search for anything']")
	search_box_element.send_keys("macmini")
	search_button_element = driver1.find_element(By.XPATH, "//input[@value='Search']")
	search_button_element.click()
	time.sleep(3)
	try :
		list_of_items = driver1.find_elements(By.CSS_SELECTOR, ".s-item__title")
	except :
		print("element not found exception")

	try :
		list_of_items_price = driver1.find_elements(By.CSS_SELECTOR, ".s-item__price")
	except :
		print("element not found exception")
	print(type(list_of_items_price))
	print(type(list_of_items))
	for title, price in zip(list_of_items, list_of_items_price) :
		print(f"{title.text} - {price.text}")
