import quandl

#    def __init__(self, key):
#        self.key = key

def quan_stock_price(api, stock):
    quandl.ApiConfig.api_key = api['quandl-key']
    data = quandl.get(stock)
    return data

def quan_dl_db(api, arg, argtwo):
    print(api)
    print(api['quandl-key'])
    quandl.ApiConfig.api_key = api['quandl-key']
    #quandl.Database("YC").bulk_download_to_file("./YC.zip")
    quandl.bulkdownload("WIKI", download_type="partial", filename="./WIKI.zip")
    return 0
