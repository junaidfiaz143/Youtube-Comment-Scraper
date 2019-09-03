from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import exceptions 
from selenium.webdriver import DesiredCapabilities
import time
import os

options = webdriver.ChromeOptions()
# options.add_argument('--headless')
# options.add_argument('start-maximized')
# options.add_argument("disable-gpu")
# options.add_argument("no-sandbox")


# options.add_argument("--window-size=1920,1080")
options.add_argument("--disable-gpu")
options.add_argument("--disable-extensions")

options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.add_argument("--proxy-bypass-list=*")
options.add_argument("start-maximized")
# options.add_argument("--headless")

capabilities = DesiredCapabilities.CHROME.copy()
capabilities['acceptSslCerts'] = True 
capabilities['acceptInsecureCerts'] = True

driver = webdriver.Chrome(executable_path=r"chromedriver.exe", options=options)

driver.get('https://www.youtube.com/watch?v=au-MlOmYX80')

driver.set_window_position(-10000, 0)

html_source = driver.page_source

# print(html_source)

time.sleep(5)
# driver.find_element_by_class_name("yt-uix-button yt-uix-button-size-default yt-uix-button-primary").click()

buttons = driver.find_elements_by_xpath('//*[@id="buttons"]/ytd-button-renderer/a')

for button in buttons:
  print(button.text)
  try:
    if str(button.text) == "SIGN IN":
      # os.system("cls")
      print("SIGN IN button class name: ", button.get_attribute("class"))
      print("SIGN IN button tag name: ", button.tag_name)
      button.click()
      print("SIGN IN button clicked")
      break
  except exceptions.SessionNotCreatedException as e:
    print("ERROR: ", e)


time.sleep(15)

driver.find_element_by_xpath('//*[@id="identifierId"]').send_keys('junaidfiaz143@gmail.com')
print("email entered")

time.sleep(2)

driver.find_element_by_xpath('//*[@id="identifierNext"]').click()
print("clicked Next button")

time.sleep(5)

driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys('')
print("password entered")

time.sleep(2)

driver.find_element_by_xpath('//*[@id="passwordNext"]').click()
print("clicked Next button")

time.sleep(5)

html_source = driver.page_source

# print(html_source)

scrollval = 500 

driver.execute_script('window.scrollTo(1, 500);')

#now wait let load the comments
time.sleep(5)

driver.execute_script('window.scrollTo(1, 3000);')


while True:
	# os.system("cls")

	comment_div = driver.find_element_by_xpath('//*[@id="contents"]')
	comments = comment_div.find_elements_by_xpath('//*[@id="content-text"]')

	# f = open("output.txt", "wb")
	for comment in comments:
		print("[COMMENT] ", comment.text)
		# f.write(("[COMMENT] " + comment.text + "\n").encode())
	# f.close()

	print("--------------")
	print(len(comments))

	driver.execute_script('window.scrollTo(1, ' + str(scrollval) + ');')

	scrollval += 500

	time.sleep(2)