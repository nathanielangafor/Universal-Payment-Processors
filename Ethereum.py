import requests

# The expected amount is in ETH meaning if you have an amount in USD you need to convert it to the ETH equivalent.
# The address is the address you want to check. I use the coinbase api to generate addresses for each transaction.

def ETH(expected, address):
    try:
        amount = requests.get('https://api.ethplorer.io/getAddressInfo/{}?apiKey=EK-noHPc-Xj9mSQb-5hLqd'.format(address)).json()['ETH']['balance']
        return float(amount) >= float(expected)
    except:
        return False
