from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import os, sys, inspect

current_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile(inspect.currentframe() ))[0]))
chromedriver = os.path.join(current_folder, "chromedriver")

driver = webdriver.Chrome(executable_path=chromedriver)
driver.get("http://google.ru")
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("py2app with custom locate chromedriver selenium working fine")
elem.send_keys(Keys.RETURN)
driver.close()
