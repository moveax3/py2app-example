import tkinter as tk
root = tk.Tk()
root.title("Test py2app tkinter")
tk.Button(root, text="Hello world!").pack()
tk.mainloop()

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://google.ru")
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("py2app with selenium working fine")
elem.send_keys(Keys.RETURN)
#driver.close()
