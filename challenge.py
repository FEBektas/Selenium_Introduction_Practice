import time
from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://www.selenium.dev/"

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(URL)

el_id = driver.find_element(By.XPATH, "/html/body/div/main/section[2]/div/div/div[1]/div/div[1]/h4")
print(f"This is the element found by id: {el_id.text}")


el_name = driver.find_element(By.NAME, "generator")
# print(f"This is the element found by Name: {el_name.text}")

# if the element has no text attribute will print out the following statement.
if el_name.text == "":
    print("Element found by name: has no text attribute")

el_xpath = driver.find_element(By.XPATH, "/html/body/div/main/section[1]/div/div/div")
# print(f"This is the element found by XPath: {el_xpath.text}")

# prints only the first 40 characters instead of the whole paragraph.
print(f"Element found by XPath: {el_xpath.text[:40]}")

el_class = driver.find_element(By.CLASS_NAME, "selenium")
print(f"This is the element found by Class: {el_class.text}")

time.sleep(3)
driver.quit()

