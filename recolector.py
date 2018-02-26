from config import *


from datetime import datetime

import numpy as np

import requests


def averagePrice(coindesk, bitstamp, cexio):
    a = [float(coindesk), float(bitstamp), float(cexio)]
    b = np.average(a)
    return b


def getResponse(url):
    r = requests.get(url)
    r.raise_for_status()
    return r.json()


class priceBTC(object):

    def getCoinDesk(cls, currency=currency):
        url = 'https://api.coindesk.com/v1/bpi/currentprice/{}.json'.format(
            currency
        )
        data = getResponse(url)
        priceCoinDesk = data['bpi'][currency]['rate_float']
        return priceCoinDesk

    def getBitstamp(cls, currency=currency):
        currency_pair = 'btc' + currency.lower()
        url = 'https://www.bitstamp.net/api/v2/ticker/{}'.format(
            currency_pair
        )
        data = getResponse(url)
        priceBitStamp = data['last']
        return priceBitStamp

    def getCexIo(cls, currency=currency):
        url = 'https://cex.io/api/last_price/BTC/{}'.format(
            currency
        )
        data = getResponse(url)
        priceCexIo = data['lprice']
        return priceCexIo
myBTC = priceBTC()

options = {
    0: myBTC.getCoinDesk(),
    1: myBTC.getBitstamp(),
    2: myBTC.getCexIo()
}


def takeValue():

    if averageMode:
        priceCD = myBTC.getCoinDesk()
        priceBS = myBTC.getBitstamp()
        priceCI = myBTC.getCexIo()
        value = averagePrice(priceCD, priceBS, priceCI)

    elif not averageMode:
        value = options[defaultExchange]
    return value
