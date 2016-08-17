import quandl

#    def __init__(self, key):
#        self.key = key

def quan_stock_price(api, stock):
    quandl.ApiConfig.api_key = api['quandl-key']
    data = quandl.get(stock)
    return data

def quan_dl_db(api):
    quandl.bulkdownload("ZEA", download_type="partial", filename="./ZEA.zip")
    return 0
