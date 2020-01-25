import requests, bs4, time

def get_crypto_price(crypto):
	"""shows current price of desired coin from coinmarketcap.com"""

	crypto_webpage = requests.get('https://coinmarketcap.com/currencies/{}/'.format(crypto))
	webpage_html = bs4.BeautifulSoup(crypto_webpage.text, 'html.parser')
	coin_price = webpage_html.find_all('span', {'class' : 'cmc-details-panel-price__price'})

	#coinmarketcap has different classes for +% and -% price chances
	coin_perc_pos = webpage_html.find_all('span', {'class' : 'cmc--change-positive cmc-details-panel-price__price-change'})
	coin_perc_neg = webpage_html.find_all('span', {'class' : 'cmc--change-negative cmc-details-panel-price__price-change'})

	if coin_perc_neg != []:
		return '{} {} {}'.format(crypto, coin_price[0].getText(), coin_perc_neg[0].getText().strip('( )'))
	elif coin_perc_pos != []:
		return '{} {} {}'.format(crypto, coin_price[0].getText(), coin_perc_pos[0].getText().strip('( )'))

def save_to_file(price_stamp):
	"""saves the current price of desired coin to a .txt file with a timestamp"""
	file = open("crypt_price.txt", "a+")

	ts = time.gmtime()

	file.write("{} {}\n".format(time.strftime("%d.%m %Y", ts),price_stamp))

coin = input("What coin are you interested in? ")
print("MEZERA")
user_input = input("Would you like to show the price or save it into a file? ")

if user_input == "show":

	print(get_crypto_price(coin))

if user_input == "save":

	save_to_file(get_crypto_price(coin))





