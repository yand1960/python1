# Получить с сайта ЦБР текущий курс доллара

from urllib import request
from http.client import HTTPResponse


class Cbr:

    def __init__(self):
        self.url_ui = "http://cbr.ru"

    def usd_rate(self):

        response: HTTPResponse = request.urlopen(self.url_ui)
        result = response.read().decode("utf-8")
        # print(result)

        pattern = '<div class="col-md-2 col-xs-9 _dollar">USD</div>'
        position = result.find(pattern)
        result = result[position: position + 200]

        pattern = "₽"
        position = result.find(pattern)
        result = result[position - 15: position]

        pattern = ">"
        position = result.find(pattern)
        result = result[position + 1: ].strip(" ")

        return float(result.replace(",", "."))

if __name__ == "__main__":
    print(Cbr().usd_rate() * 2)