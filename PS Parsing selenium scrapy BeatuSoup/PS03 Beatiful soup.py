from bs4 import BeautifulSoup
import requests

url = "http://quotes.toscrape.com/"
response = requests.get(url)
html = response.text # получаем html код

soup = BeautifulSoup(html, "html.parser") #парсим html код





text = soup.find_all("span", class_="text") #находим нужную нам информацию
print(text)

author = soup.find_all("small", class_="author")
print(author)

for i in range(len(text)): #перебираем элементы в списке и нумеруем их
    print(f" Цитата номер - {i+1}")
    print(text[i].text)
    print(author[i].text)








# links = soup.find_all("a") #получаем все ссылки
# for link in links:
#     print(link.get("href")) #выводим все ссылки
