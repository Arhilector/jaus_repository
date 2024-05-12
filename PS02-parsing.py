import requests
import pprint

url = 'https://jsonplaceholder.typicode.com/posts'

params = {

    "userId" : 22
}

response = requests.post(url, params=params)

print(response.status_code)

if response.status_code == 201:
    posts = response.json()
    for post in posts:
        print(post)
else:
    print("Error")





# url = 'https://jsonplaceholder.typicode.com/posts'
#
# data = {
#     "title" :  "foo",
#     "body" : "bar",
#     "userId" : 1
# }
#
# response = requests.post(url, data=data)
#
# print(response.status_code)
#
# print(f"ответ - {response.json()}")










# #скачивание  изображения
# img = "https://get.wallhere.com/photo/landscape-mountains-lake-nature-reflection-grass-sky-river-national-park-valley-wilderness-Alps-tree-autumn-leaf-mountain-season-tarn-loch-mountainous-landforms-mountain-range-590185.jpg"
#
# responce = requests.get(img)
#
# with open('test.jpg', 'wb') as file:
#     file.write (responce.content)




#извлекание данных json
# params = {
#     'q': 'HTML',
# }
#
# responce = requests.get('https://api.github.com/search/repositories', params=params)
#
# responce_json = responce.json()
# pprint.pprint(responce_json)
#
# print(f"количество репозиториев с использованием HTML: {responce_json['total_count']}")













# responce = requests.get('https://api.github.com/')
# print (responce.status_code)
# print (responce.ok)
# if responce.ok:
#     print ("запрос выполнен успешно")
# else:
#     print ("запрос не выполнен")
#
# print(responce.text)
#
# responce_json = responce.json()
# pprint.pprint(responce_json)
