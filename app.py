from flask import Flask, request, render_template, jsonify
from selenium import webdriver
import time
import os

# url = "https://www.youtube.com/watch?v=au-MlOmYX80"

url = ""

options = webdriver.ChromeOptions()
# options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")

def get_comments(url):

		driver = webdriver.Chrome(executable_path=r"chromedriver.exe", chrome_options=options)
		driver.get(url)
		scrollval = 500 

		driver.execute_script('window.scrollTo(1, 500);')

		#now wait let load the comments
		time.sleep(5)

		driver.execute_script('window.scrollTo(1, 3000);')

		while True:

			comment_div = driver.find_element_by_xpath('//*[@id="contents"]')
			comments = comment_div.find_elements_by_xpath('//*[@id="content-text"]')

			final_comments = []

			for comment in comments:
				final_comments.append(comment.text)

			if scrollval == 10000:
				return final_comments

			driver.execute_script('window.scrollTo(1, ' + str(scrollval) + ');')

			scrollval += 500

			time.sleep(2)

app = Flask(__name__)

@app.route("/", methods=["GET", 'POST'])
def home():
	if request.method == "POST":
		url = request.form["url"]
		print(url)

		return jsonify(comments=get_comments(url))

	return render_template("index.html")

if __name__ == "__main__":
	app.run(debug=True)