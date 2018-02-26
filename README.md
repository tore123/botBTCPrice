# botBTCPrice
<b> This Telegram bot will help you get the current bitcoin quote price on the populars exchanges. </b> 

<img border="0"  src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Bitcoin.svg/240px-Bitcoin.svg.png" width="150" height="150">

[![Travis](https://travis-ci.org/tore123/botBTCPrice.svg?branch=master)]()
[![Packagist](https://img.shields.io/packagist/l/doctrine/orm.svg)]()

| Full name | Telegram bot for Bitcoin Price |
|-----------|--------------------------------|
| Author    | Aitor Velasco                  |
| Version   | 2.0.0                          |

</br>

<h2> What it is </h2> 
This Telegram bot will help you get the current bitcoin quote price on the popular Coin Desk platform anytime you want. 

<h2> What's new in version 2?</h2> 
In this new version you can get the average price of Bitcoin base on the different exchange for get an better value market using the average mode. Too you can configure new params for simple mode (not average mode), for example change your default exchange.


<h2> How to use it </h2>
Simple, once you have entered the basic bot parameters such as the token obtained by @botFather, type in your Telegram application <b> /price </b>  to get the most recent updated price. Enter the token between the quotation marks of the config.py file

<h2> Customize parameters </h2>
You are free to configure your own parameters such as currency, decimals or the action command used in config.py file. </br>
<b> decimals </b>: Allow change the number of decimals for you respone, by default is 2 </br>
<b> currency </b>: Allow change the fiat currence, use always capital letters for this params, by default is EUR  </br>
<b> token </b>: This is your token from @BotFather  </br>
<b> command </b>: This is the command for interact with the bot for get the value of Bitcoin, By default is price. </br>
<b> defaultExchange </b>: Allow  change the exchange for not-average mode 0 = coindesk 1 = bitstamp 2 = cex.io. By default is 0 </br>
<b> averageMode </b>: Allow activate the averageMode. By default is True </br>

<h2> TO-DO </h2>
- 1 - Add new cryptocurrences like ether or monero </br>
- 2 - Add custom commands for every cryptocurrence from Telegram bot </br>
- 3 - Add a Telegram menu for change all params without code </br>
- 4 - Add more Exchanges like Coinbase </br>

<h2> Contributors </h2>
You are free to join me for contribute to this project reporting bugs, coding or sending ideas please feel free contact me!.
