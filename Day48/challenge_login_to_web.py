from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

chrome_driver_path = 'D:\Developers\chromedriver_win32\chomedriver.exe'
chrome_options = Options()
chrome_options.add_experimental_option('detach',True)   #Avoids Selenium to close the browser
driver = webdriver.Chrome(executable_path=chrome_driver_path,chrome_options=chrome_options)

driver.get('https://www.amazon.com')
search = driver.find_element(By.NAME,'field-keywords')
#password = driver.find_element(By.NAME,'password')
#login_button = driver.find_element(By.NAME,'commit')

search.send_keys('Harry Potter Crocs')
search.send_keys(Keys.ENTER)

#password.send_keys('123qwerty')
#login_button.click()


