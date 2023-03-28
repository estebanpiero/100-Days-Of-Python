#import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_driver_path = 'D:\Developers\chromedriver_win32\chomedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver_path)

#driver.get('https://www.amazon.com/Crocs-Unisex-Classic-Bradley-Potter/dp/B0B5P9DYRK/?_encoding=UTF8&pd_rd_w=uIm7m&content-id=amzn1.sym.08900ed4-dd64-49b1-bce7-2e717defb1aa&pf_rd_p=08900ed4-dd64-49b1-bce7-2e717defb1aa&pf_rd_r=E19AJK5KSG51KBVVGFMR&pd_rd_wg=LyDjW&pd_rd_r=2b70960f-073c-47f2-955e-fed79e3aee8f&ref_=pd_gw_ci_mcx_mi')
#prices = driver.find_element(By.ID ,'corePrice_desktop')
#price = driver.find_element(By.CLASS_NAME ,'a-price')
#print(price.text)

driver.get('https://www.python.org/')

events_times = driver.find_elements(By.CSS_SELECTOR,'.event-widget time')
events_names = driver.find_elements(By.CSS_SELECTOR,'.event-widget li a')

events = {}

for n in range(len(events_times)):
    events[n] = {
        'times': events_times[n].text,
        'names': events_names[n].text
    }

print(events)


driver.close()
