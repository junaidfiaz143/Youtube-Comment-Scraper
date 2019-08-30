from selenium import webdriver
import time
import os

options = webdriver.ChromeOptions()
# options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")

driver = webdriver.Chrome(executable_path=r"chromedriver.exe", chrome_options=options)
driver.get('https://www.youtube.com/watch?v=au-MlOmYX80')

# driver.set_window_position(-10000,0)

html_source = driver.page_source

# print(html_source)

scrollval = 500 

driver.execute_script('window.scrollTo(1, 500);')

#now wait let load the comments
time.sleep(5)

driver.execute_script('window.scrollTo(1, 3000);')


while True:
	os.system("cls")

	comment_div = driver.find_element_by_xpath('//*[@id="contents"]')
	comments = comment_div.find_elements_by_xpath('//*[@id="content-text"]')

	f = open("output.txt", "wb")
	for comment in comments:
		print("[COMMENT] ", comment.text)
		f.write(("[COMMENT] " + comment.text + "\n").encode())
	f.close()

	print("--------------")
	print(len(comments))

	driver.execute_script('window.scrollTo(1, ' + str(scrollval) + ');')

	scrollval += 500

	time.sleep(2)