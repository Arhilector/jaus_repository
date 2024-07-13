import scrapy
import os

# Определение класса для паука
class DivannewparsSpider(scrapy.Spider):
    name = "divannewpars"  # Имя паука
    allowed_domains = ["https://divan.ru"]  # Разрешенные домены для обхода
    start_urls = ["https://www.divan.ru/category/svet"]  # URL для начального запроса

    custom_settings = {
        'FEEDS': {
            'C:\\Users\\Professional\\Documents\\GitHub\\jaus_repository\\divanpars\\divanpars\\spiders\\PARSING-DIVAN.csv': {
                'format': 'csv',
                'encoding': 'utf8',
                'store_empty': False,
                'fields': ['name', 'price', 'url'],
                'overwrite': True
            }
        }
    }

    def parse(self, response):
        """
        Метод для обработки ответа от начального URL.
        """
        # Выбор всех элементов, содержащих информацию о светильниках
        lights = response.css('div._Ud0k')

        # Итерация по каждому элементу
        for light in lights:
            # Извлечение данных и их генерация в виде словаря
            yield {
                'name': light.css('div.lsooF span::text').get(),  # Извлечение имени светильника
                'price': light.css('div.pY3d2 span::text').get(),  # Извлечение цены светильника
                'url': light.css('a').attrib['href']  # Извлечение URL светильника
            }
