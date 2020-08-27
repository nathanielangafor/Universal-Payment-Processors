import requests
import bs4 as bs

# The expected amount is in ETC meaning if you have an amount in USD you need to convert it to the ETC equivalent.
# The address is the address you want to check. I use the coinbase api to generate addresses for each transaction.

def ETC(expected, address):
    try:
        r = requests.get('https://receipt.emerald.cash/balance/{}'.format(address))
        soup = bs.BeautifulSoup(r.text, 'lxml')
        balance = soup.findAll('div', attrs={'class': 'col-md-8 col-10 text-right'})[1].text
        return float(balance) >= float(expected)
    except:
        return False