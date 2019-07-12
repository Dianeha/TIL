from iexfinance.stocks import Stock

token = 'pk_63c229409ff14b67a6cc81e38927f1c4'
stock = Stock('TSLA', token=token).get_quote()
company_name = stock['companyName']
lastest_price = stock['iexRealtimePrice']

print(company_name)
print(lastest_price)
print(type(lastest_price))
print(lastest_price*120.1)