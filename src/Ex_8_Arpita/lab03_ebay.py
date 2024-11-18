'''Task 22nd October,2024
Open the Url -www.ebay.com/b/Desktops-All-In-One-Computers/171957/bn_1643067
Search for the Macmini
Click on the search ICON
Get all the titles
Get al the prices
Print all the titles and prices in the end. (side by side)
Find the Max and Min price also (from the list)'''

import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_price_item ( ) :
	global list_of_items, list_of_items_price

	print("AAAAAAAAAAAAAAAAAAAAAAa")
	driver = webdriver.Chrome()  # Make sure you have the appropriate WebDriver installed and in PATH
	driver.maximize_window()
	driver.get('https://www.ebay.com/b/Desktops-All-In-One-Computers/171957/bn_1643067')
	time.sleep(3)
	search_box = driver.find_element(By.XPATH, "//input[@placeholder = 'Search for anything']")
	search_box.send_keys('macmini')
	search_button = driver.find_element(By.XPATH, "//input[@value='Search']")
	search_button.click()
	print("---bbbbbbbbbbbbbbbbb----")
	time.sleep(3)  # Wait for the results to load
	list_of_items = driver.find_elements(By.XPATH, "//div[@class='s-item__title']")
	list_of_items_price = driver.find_elements(By.XPATH, "//span[@class='s-item__price']")

	print("---CCCCCCCCCCCCCCCCCCC----")
	print(type(list_of_items_price))
	print(type(list_of_items))
	time.sleep(2)
	for title, price in zip(list_of_items, list_of_items_price) :
		print(f"{title.text} - {price.text}")
