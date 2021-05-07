import requests
from bs4 import BeautifulSoup
import time


class Curency:
    Tesla = 'https://www.google.ru/search?q=%D1%86%D0%B5%D0%BD%D0%B0+%D0%B0%D0%BA%D1%86%D0%B8%D0%B8+%D1%82%D0%B5%D1' \
            '%81%D0%BB%D0%B0&newwindow=1&safe=strict&sxsrf=ALeKk02vRIY0BD5Opvl7_RH6i9SI4xnXew%3A1618656421081&source' \
            '=hp&ei=pLx6YM7DN-eIrwT9uKH4DQ&iflsig=AINFCbYAAAAAYHrKteOE94HOc6XPdOIP8X1JamlA8KCU&oq=%D1%86%D0%B5%D0%BD' \
            '%D0%B0+%D0%B0%D0%BA%D1%86%D0%B8%D0%B8+&gs_lcp' \
            '=Cgdnd3Mtd2l6EAEYADIHCAAQRhD6ATICCAAyAggAMgIIADICCAAyAggAMgIIADICCAAyAggAMgIIADoFCAAQsQM6CwgAELEDEMcBEK8BOggILhCxAxCDAToICAAQsQMQgwE6CwgAELEDEMcBEKMCOgUILhCxAzoICAAQsQMQyQM6CAgAEMcBEK8BOg4IABCxAxCDARDHARCjAjoKCAAQsQMQRhCCAjoFCAAQyQNQqVpY0G9g-oABaABwAHgAgAFOiAGxBZIBAjExmAEAoAEBqgEHZ3dzLXdpeg&sclient=gws-wiz '
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0'}

    current_converted_price = 0
    buy_price = 0
    sell_price = 0

    def __init__(self):
        self.current_converted_price = float(self.get_currency_price().replace(",", "."))
        print("Укажите цену, за которую хотите купить акцию: ")
        self.buy_price = float(input())
        print("Укажите цену, за которую хотите продать акцию: ")
        self.sell_price = float(input())

    def get_currency_price(self):
        full_page = requests.get(self.Tesla, headers=self.headers)
        soup = BeautifulSoup(full_page.content, 'html.parser')
        convert = soup.find_all("span", {"class": "IsqQVc NprOob XcVN5d wT3VGc", "jsname": "vWLAgc"})
        return convert[0].text

    def check_currency(self):
        currency = float(self.get_currency_price().replace(",", "."))

        if currency >= self.sell_price:
            print("1 акция Теслы стоит " + str(currency) + "$")
            print("ПРОДАВАЙТЕ")
            return

        elif currency <= self.buy_price:
            print("1 акция Теслы стоит " + str(currency) + "$")
            print("ПОКУПАЙТЕ")
            return

        print("1 акция Теслы стоит " + str(currency) + "$")
        time.sleep(20)
        self.check_currency()
