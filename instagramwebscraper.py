# Selenium imports here

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

# specify the path to chromedriver.exe (download and save on your computer)
driver = webdriver.Chrome('C:/Users/atgra/Downloads/chromedriver_win32 (1)/chromedriver.exe')

# open the webpage
driver.get("http://www.instagram.com")

# Accept cookies
acceptAll = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Accept All')]"))).click()

# target username
username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

# enter username and password
username.clear()
username.send_keys("alan_grahm")
password.clear()
password.send_keys("Maywalker0512")

# target the login button and click it
button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

# dismiss pop up
dismissPopup = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]"))).click()
dismissPopup2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]"))).click()

# Enter keyword
searchBox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search']")))
searchBox.clear()
keyword = "#cat"
searchBox.send_keys(keyword)



# press enter
searchBox.send_keys(Keys.ENTER)
searchBox.send_keys(Keys.ENTER) 


driver.execute_script("window.scrollTo(0,4000);")

images = driver.find_elements_by_tag_name('img')
