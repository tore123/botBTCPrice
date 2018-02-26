from config import *


from datetime import datetime

import requests


def getResponse(url):
    r = requests.get(url)
    r.raise_for_status()
    return r.json()


class getCoinDesk(object):

    def getCurrentPrice(cls, currency=currency):
        url = 'https://api.coindesk.com/v1/bpi/currentprice/{}.json'.format(
            currency
        )
        data = getResponse(url)
        priceBTC = data['bpi'][currency]['rate_float']
        return priceBTC



