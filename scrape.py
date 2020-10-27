from selenium import webdriver
from selenium.webdriver.common.by import By
from contextlib import closing
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Firefox
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import urllib2
import re
from bs4 import BeautifulSoup
import unicodedata
from selenium.webdriver.firefox.options import Options

# adding options to browser
opt = Options()
opt.add_argument("--disable-infobars")
opt.add_argument("start-maximized")
opt.add_argument('--no-sandbox')

# To manage permissions uncomment these lines.
# opt.add_experimental_option("prefs", {
#                                         "profile.default_content_setting_values.media_stream_mic": 1,
#                                         "profile.default_content_setting_values.media_stream_camera": 1,
#                                         "profile.default_content_setting_values.geolocation": 2,
#                                         "profile.default_content_setting_values.notifications": 2,
# })
# opt.add_argument("--disable-extensions")

def remove_non_ascii_1(text):

    return ''.join([i if ord(i) < 128 else ' ' for i in text])

with closing(Firefox(options=opt)) as browser:
	site = "https://www.flipkart.com/asus-zenfone-2-laser-ze550kl-black-16-gb/product-reviews/itme9j58yzyzqzgc?pid=MOBE9J587QGMXBB7"
	browser.get(site)

	file = open("review.txt", "w")

	for count in range(1, 10):
		nav_btns = browser.find_elements_by_class_name('_33m_Yg')

		button = ""

		for btn in nav_btns:
			number = int(btn.text)
			if(number==count):
				button = btn
				break

		button.send_keys(Keys.RETURN)
		WebDriverWait(browser, timeout=10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "_2xg6Ul")))

		read_more_btns = browser.find_elements_by_class_name('_1EPkIx')
		

		for rm in read_more_btns:
			browser.execute_script("return arguments[0].scrollIntoView();", rm)
			browser.execute_script("window.scrollBy(0, -150);")
			rm.click()

		page_source = browser.page_source

		soup = BeautifulSoup(page_source, "lxml")
		ans = soup.find_all("div", class_="_3DCdKt")


		for tag in ans:
			title = unicode(tag.find("p", class_="_2xg6Ul").string).replace(u"\u2018", "'").replace(u"\u2019", "'")
			title = remove_non_ascii_1(title)
			title.encode('ascii','ignore')
			content = tag.find("div", class_="qwjRop").div.prettify().replace(u"\u2018", "'").replace(u"\u2019", "'")
			content = remove_non_ascii_1(content)
			content.encode('ascii','ignore')
			content = content[15:-7]

			votes = tag.find_all("span", class_="_1_BQL8")
			upvotes = int(votes[0].string)
			downvotes = int(votes[1].string)

			file.write("Review Title : %s\n\n" % title )
			file.write("Upvotes : " + str(upvotes) + "\n\nDownvotes : " + str(downvotes) + "\n\n")
			file.write("Review Content :\n%s\n\n\n\n" % content )

	file.close()

