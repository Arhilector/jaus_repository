from selenium import webdriver
import time


browser = webdriver.Chrome()
browser.get("https://www.arhilector.ru")
browser.save_screenshot("arhilector.png")
time.sleep(10)
browser.get("https://ru.wikipedia.org/wiki/Заглавная_страница")
browser.save_screenshot("wikipedia.png")
time.sleep(10)
browser.refresh()
