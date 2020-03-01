import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time



# Set headers
headers = requests.utils.default_headers()
headers.update({ 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})

url = "https://github.com/rock6064/text/blob/master/text.txt"
req = requests.get(url, headers)
soup = BeautifulSoup(req.content, 'html.parser')

rohan = soup.find(id="LC1").text
print(rohan)



desired_cap = {
 'browser': 'Chrome',
 'browser_version': '80.0',
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
