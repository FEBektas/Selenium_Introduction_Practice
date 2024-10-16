from selenium import webdriver
from selenium.webdriver.common.by import By
import time

URL = "https://ultimateqa.com/filling-out-forms/"

driver = webdriver.Chrome()
driver.get(URL)

# finding elements!
name = driver.find_element(By.ID, "et_pb_contact_name_1")
message = driver.find_element(By.ID, "et_pb_contact_message_1")
sum_field = driver.find_element(By.XPATH, "//*[@id='et_pb_contact_form_1']/div[2]/form/div/div/p/input")
button = driver.find_element(By.XPATH, "//*[@id='et_pb_contact_form_1']/div[2]/form/div/button")
captcha = driver.find_element(By.CLASS_NAME, "et_pb_contact_captcha_question")

# element interactions!

# inserts the string into the intended fields.
name.send_keys("Bektas")
message.send_keys("Hello, this is an automated test script")
text = captcha.text
# print(text)

# splits the calculation (6+1) into a list.
number_list = text.split()
# print(number_list)

# takes the first index from the list and the second index from the list, transforms from str into int and
# calculates the correct operation.
result = int(number_list[0]) + int(number_list[2])
# print(result)

# inputs the result from the calculation into the intended field.
sum_field.send_keys(str(result))
button.click()

time.sleep(3)
driver.quit()
