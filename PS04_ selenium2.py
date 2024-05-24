from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

import time

browser = webdriver.Chrome()
browser.get("https://ru.wikipedia.org/w/index.php?go=Перейти&search=солнечная+система&title=Служебная%3AПоиск&ns0=1")

time.sleep(3)

assert "Википедия" in browser.title  # Проверка наличия заголовка

search_box = browser.find_element(By.ID, "searchInput")

search_box.send_keys("Солнечная система")  # Поиск по слову "Солнечная система"

time.sleep(3)

search_box.send_keys(Keys.RETURN)

time.sleep(3)

a = browser.find_element(By.LINK_TEXT, "Солнечная система")
a.click()
time.sleep(10)