from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common import exceptions 
from selenium.webdriver import DesiredCapabilities
# import time
# import os

options = webdriver.ChromeOptions()
# options.add_argument('--headless')
# options.add_argument('start-maximized')
# options.add_argument("disable-gpu")
# options.add_argument("no-sandbox")


# options.add_argument("--window-size=1920,1080")
options.add_argument("--disable-gpu")
options.add_argument("--disable-extensions")

options.add_argument('--ignore-certificate-errors')
# options.add_argument("--test-type")
options.add_argument("--proxy-bypass-list=*")
options.add_argument("start-maximized")
# options.add_argument("--headless")

# chrome_options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ['enable-automation'])
prefs = {"credentials_enable_service": False}

# print(prefs)
# options.add_experimental_option("prefs", prefs)
# prefs = {"profile.password_manager_enabled": False}

options.add_experimental_option("prefs", prefs)
# driver = webdriver.Chrome(options=chrome_options);  

capabilities = DesiredCapabilities.CHROME.copy()
capabilities['acceptSslCerts'] = True 
capabilities['acceptInsecureCerts'] = True

driver = webdriver.Chrome(executable_path=r"chromedriver.exe", options=options)

driver.get('https://www.juglo.pk/vendor.php?dispatch=auth.login_form&return_url=vendor.php')

# driver.set_window_position(-10000, 0)

# html_source = driver.page_source

# wait = WebDriverWait(driver, 10);

# print(html_source)
while True:
	try:
		input_email = driver.find_element_by_xpath('//*[@name="user_login"]').send_keys('techhuborignal@gmail.com')
		input_email = driver.find_element_by_xpath('//*[@name="password"]').send_keys('techhub12@')

		driver.find_element_by_xpath('//*[@value="Sign in"]').click()
		break
	except:
		continue

# driver.execute_script('')