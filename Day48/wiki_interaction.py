from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

chrome_driver_path = 'D:\Developers\chromedriver_win32\chomedriver.exe'
chrome_options = Options()
chrome_options.add_experimental_option('detach',True)   #Avoids Selenium to close the browser
driver = webdriver.Chrome(executable_path=chrome_driver_path,chrome_options=chrome_options)

#driver.get('https://en.wikipedia.org/wiki/Main_Page')
#count = driver.find_element(By.CSS_SELECTOR,'#articlecount a')
#all_portals = driver.find_element(By.PARTIAL_LINK_TEXT,'Two earthquakes')
#all_portals.click()

driver.get('https://en.wikipedia.org/w/index.php?search=&title=Special:Search')
search = driver.find_element(By.NAME,'search')
search.click()
search.send_keys('Python')
search.send_keys(Keys.ENTER)