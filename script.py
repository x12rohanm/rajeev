import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import random


# Set headers
headers = requests.utils.default_headers()
headers.update({ 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})

url = "https://github.com/rock6064/text/blob/master/text.txt"
req = requests.get(url, headers)
soup = BeautifulSoup(req.content, 'html.parser')

rohan = soup.find(id="LC1").text
print(rohan)

versions = ['79.0', '78.0', '77.0', '76.0', '75.0', '74.0', '73.0', '72.0', '71.0', '70.0', '69.0', '68.0', '67.0', '66.0', '65.0', '64.0', '63.0', '62.0', '61.0', '60.0', '59.0', '58.0', '57.0', '56.0', '55.0', '54.0', '53.0', '52.0', '51.0', '50.0', '49.0', '48.0', '47.0']
selected_version = random.choice(versions)
print(f'Selected Browser Version:- {selected_version}')


desired_cap = {
 'browser': 'Chrome',
 'browser_version': selected_version,
 'os': 'OS X',
 'os_version': 'Catalina',
 'resolution': '1600x1200',
 'name': 'Bstack-[Python] Sample Test'
}

driver = webdriver.Remote(
    command_executor=rohan,
    desired_capabilities=desired_cap)


driver.get("http://www.ebesucher.com/surfbar/rock6064")
time.sleep(10)
driver.find_element_by_id("surf_now_button").click()
print("Started...")
driver.switch_to.window(driver.window_handles[1])
time.sleep(70)
driver.switch_to.window(driver.window_handles[0])
time.sleep(5)
driver.switch_to.window(driver.window_handles[1])
time.sleep(70)
driver.switch_to.window(driver.window_handles[0])
time.sleep(5)
driver.switch_to.window(driver.window_handles[1])
time.sleep(70)
driver.switch_to.window(driver.window_handles[0])
time.sleep(5)
driver.switch_to.window(driver.window_handles[1])
time.sleep(70)
driver.switch_to.window(driver.window_handles[0])
time.sleep(5)
driver.switch_to.window(driver.window_handles[1])
time.sleep(70)
driver.switch_to.window(driver.window_handles[0])
time.sleep(5)
driver.switch_to.window(driver.window_handles[1])
time.sleep(70)
driver.switch_to.window(driver.window_handles[0])
time.sleep(5)
driver.switch_to.window(driver.window_handles[1])
time.sleep(70)
driver.switch_to.window(driver.window_handles[0])
time.sleep(5)
driver.switch_to.window(driver.window_handles[1])
time.sleep(70)
driver.switch_to.window(driver.window_handles[0])
time.sleep(5)
driver.switch_to.window(driver.window_handles[1])
time.sleep(70)
driver.switch_to.window(driver.window_handles[0])
time.sleep(5)
driver.switch_to.window(driver.window_handles[1])
time.sleep(70)
driver.switch_to.window(driver.window_handles[0])
time.sleep(5)
driver.switch_to.window(driver.window_handles[1])
time.sleep(70)
driver.switch_to.window(driver.window_handles[0])
time.sleep(5)
driver.switch_to.window(driver.window_handles[1])
time.sleep(70)
driver.switch_to.window(driver.window_handles[0])
time.sleep(5)
driver.switch_to.window(driver.window_handles[1])
time.sleep(70)
driver.switch_to.window(driver.window_handles[0])
time.sleep(5)
driver.switch_to.window(driver.window_handles[1])
time.sleep(70)
driver.switch_to.window(driver.window_handles[0])
time.sleep(5)
driver.switch_to.window(driver.window_handles[1])
time.sleep(70)
driver.switch_to.window(driver.window_handles[0])
time.sleep(5)
driver.switch_to.window(driver.window_handles[1])
time.sleep(70)
driver.switch_to.window(driver.window_handles[0])
time.sleep(5)
driver.switch_to.window(driver.window_handles[1])
time.sleep(70)





driver.close()
driver.switch_to.window(driver.window_handles[0])
time.sleep(3)






driver.quit()
print("Done...")
