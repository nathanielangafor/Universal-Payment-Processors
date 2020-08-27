from blockcypher import get_address_overview

# The expected amount is in BTC meaning if you have an amount in USD you need to convert it to the BTC equivalent.
# The address is the address you want to check. I use the coinbase api to generate addresses for each transaction.

def BTC(expected, address):
    try:
        return float(get_address_overview(address)['total_received']) * .00000001 >= float(expected)
    except:
        return False

