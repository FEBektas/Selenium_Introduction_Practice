from selenium import webdriver
from selenium.webdriver.common.by import By
import time

URL = "https://ultimateqa.com/filling-out-forms/"

driver = webdriver.Chrome()
driver.get(URL)

# first, finding elements!
name = driver.find_element(By.ID, "et_pb_contact_name_0")
message = driver.find_element(By.ID, "et_pb_contact_message_0")
button = driver.find_element(By.NAME, "et_builder_submit_button")

# clear form fields!
name.clear()
message.clear()

# sending data!
message.send_keys("Hello, and wellcome to my first automated script!")
name.send_keys("Erkan")

# other element actions!
button.click()

time.sleep(3)

# closing all webdriver instances.
driver.quit()
