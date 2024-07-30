from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import random
import time

browser = webdriver.Chrome()
browser.get("https://ru.wikipedia.org/w/index.php?go=Перейти&search=солнечная+система&title=Служебная%3AПоиск&ns0=1")

hatnotes = []

for element in browser.find_elements(By.TAG_NAME, "div"):
    # Чтобы искать атрибут класса
    cl = element.get_attribute("class")
    if cl == "hatnote navigation-not-searchable":
        hatnotes.append(element)

print(hatnotes)
hatnote = random.choice(hatnotes)

# Для получения ссылки мы должны найти на сайте тег "a" внутри тега "div"
link = hatnote.find_element(By.TAG_NAME, "a").get_attribute("href")
browser.get(link)
time.sleep(30)





# time.sleep(10)
#
# paragraphs = browser.find_elements(By.TAG_NAME, "p")
#
# for paragraph in paragraphs:
#     print(paragraph.text)
#     input()


