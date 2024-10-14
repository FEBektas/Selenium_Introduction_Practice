import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# python.org website
URL = "https://www.python.org/"


# webdriver frp CHROME.
driver = webdriver.Chrome()
driver.get(URL)

# finding the "search" bar in the python website with the name "q".
search = driver.find_element(By.NAME, "q")

# clears the field if maybe there is something already written.
search.clear()

# in the search bar types the "pycon"  text.
time.sleep(2)
search.send_keys("pycon")

# presses enter.
search.send_keys(Keys.RETURN)

# driver.quit will close all instances when driver.close will only close the focused window.
time.sleep(3)
driver.quit()
