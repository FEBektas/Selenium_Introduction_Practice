import time
from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://wiki.python.org/moin/FrontPage"

driver = webdriver.Chrome()
# driver.fullscreen_window()
driver.get(URL)

# finding elements.
text = driver.find_element(By.ID, "searchinput")

# interactions
text.send_keys("Beginner")

time.sleep(1)
driver.find_element(By.ID, "fullsearch").click()

time.sleep(2)

# drop_down
driver.find_element(By.XPATH, "//*[@id='sidebar']/div[3]/ul/li[5]/form/div/select").click()

# drop_down element*
time.sleep(1)
driver.find_element(By.XPATH, "//*[@id='sidebar']/div[3]/ul/li[5]/form/div/select/option[2]").click()

time.sleep(2)
driver.quit()
