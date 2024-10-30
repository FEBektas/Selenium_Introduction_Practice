import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

URL = "https://practice.expandtesting.com/login"

driver = webdriver.Chrome()
driver.get(URL)
driver.fullscreen_window()

# locate_elements by ID.
login_username = driver.find_element(By.ID, "username")
login_password = driver.find_element(By.ID, "password")

# locate_elements by CLASS.
# login_username = driver.find_element(By.CLASS_NAME, "username")

# locate_elements by NAME.
# login_password = driver.find_element(By.NAME, "password")

# locate_elements by LINK TEXT.
# login_username = driver.find_element(By.LINK_TEXT, "username")

# locate_elements by PARTIAL LINK TEXT.
# login_password = driver.find_element(By.PARTIAL_LINK_TEXT, "password")

# locate_elements by TAG NAME.
# login_username = driver.find_element(By.TAG_NAME, "username")

# locate_elements by XPath.

# XPath = //tag name[@attribute = 'Value']
# // -> used to select current node in the document
# Tag name -> name of the tag of a particular node
# @ -> it selects attributes like id, name, className, etc.
# Attribute -> node's attribute name like type, class, name, id, etc.
# Value -> value of that attribute




# clear field.
login_username.clear()
login_password.clear()

# send text.
login_username.send_keys("practice")
login_password.send_keys("SuperSecretPassword!")

# press enter
login_password.send_keys(Keys.RETURN)


time.sleep(3)
driver.quit()