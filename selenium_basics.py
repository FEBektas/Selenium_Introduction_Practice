import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# URL - is the url of the site you want to test from.
URL = "https://www.python.org/"


# driver = ....Chrome - to create a variable to run the test on the Chrome browser.
driver = webdriver.Chrome()

# driver = ....Edge - to create a variable to run the test on the Edge browser.
driver1 = webdriver.Edge()

# .get() - will paste the url on the specific browser named by the specific variable.
driver.get(URL)
driver1.get(URL)

# .find_element - will search on the url for the specific HTML syntax you input.
elem = driver.find_element(By.NAME, "q")
elem1 = driver1.find_element(By.NAME, "q")

# .clear - will clear the field if by any chance it will have anything in it.
elem.clear()
elem1.clear()

# .send_keys - will type the intended string and will search it in the .find_element variable.
elem.send_keys("pycon")
time.sleep(2) # will let the input with the intended word for the time inserted.
elem1.send_keys("erkan")
time.sleep(2)

# .send_keys - will press enter.
elem.send_keys(Keys.RETURN)
elem1.send_keys(Keys.RETURN)

# .quit will end the background process
driver1.quit()
time.sleep(4)
driver.quit()
time.sleep(4)
