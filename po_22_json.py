# Получить курс доллара от веб службы ЦБР
# (путем десериализации json)

from urllib import request
from http.client import HTTPResponse
import json


def rate(currency):

    url_ws = "https://www.cbr-xml-daily.ru/daily_json.js"

    response: HTTPResponse = request.urlopen(url_ws)
    result = response.read().decode("utf-8")
    rates = json.loads(result)
    try:
        return rates['Valute'][currency]['Value']
    except KeyError:
        raise KeyError(f"Данных о валюте {currency} нет")


if __name__ == "__main__":
    print(rate("USD"), rate("AZN"))