# Получить курс доллара от веб службы ЦБР
# (путем десериализации json)

from urllib import request
from http.client import HTTPResponse
import json
from po_21_urllib import Cbr


class CbrAggregated(Cbr):

    def __init__(self):
        self.url_ws = "https://www.cbr-xml-daily.ru/daily_json.js"
        super().__init__()

    def rate(self, currency):

        response: HTTPResponse = request.urlopen(self.url_ws)
        result = response.read().decode("utf-8")
        rates = json.loads(result)
        try:
            return rates['Valute'][currency]['Value']
        except KeyError:
            raise KeyError(f"Данных о валюте {currency} нет")


if __name__ == "__main__":
    cbr_aggregated = CbrAggregated()
    print( cbr_aggregated.rate("USD"), cbr_aggregated.usd_rate())