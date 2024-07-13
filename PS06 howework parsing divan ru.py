import scrapy
import csv
import os


class DivannewparsSpider(scrapy.Spider):
    name = "divannewpars"
    allowed_domains = ["divan.ru"]
    start_urls = ["https://www.divan.ru/category/svet"]

    def __init__(self, *args, **kwargs):
        super(DivannewparsSpider, self).__init__(*args, **kwargs)
        self.file_path = os.path.join(os.getcwd(), 'divanpars.csv')
        try:
            self.csv_file = open(self.file_path, 'w', newline='', encoding='utf-8')
            self.csv_writer = csv.writer(self.csv_file)
            self.csv_writer.writerow(['name', 'price', 'url'])
        except Exception as e:
            self.logger.error(f"Failed to open file {self.file_path}: {e}")
            raise e

    def closed(self, reason):
        self.csv_file.close()

    def parse(self, response):
        lights = response.css('div._Ud0k')

        for light in lights:
            name = light.css('div.lsooF span::text').get()
            price = light.css('div.pY3d2 span::text').get()
            url = light.css('a').attrib['href']

            try:
                self.csv_writer.writerow([name, price, url])
            except Exception as e:
                self.logger.error(f"Failed to write to CSV: {e}")

            yield {
                'name': name,
                'price': price,
                'url': url
            }