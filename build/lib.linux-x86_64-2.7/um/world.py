import wbpy
from pprint import pprint

#>>> import wbpy
#>>> from pprint import pprint
#>>> 
#>>> api = wbpy.IndicatorAPI()
#>>> 
#>>> iso_country_codes = ["GB", "FR", "JP"]
#>>> total_population = "SP.POP.TOTL"
#>>> 
#>>> dataset = api.get_dataset(total_population, iso_country_codes, date="2010:2012")
#>>> dataset
#<wbpy.indicators.IndicatorDataset(u'SP.POP.TOTL', u'Population, total') with id: 140637080086864>
#>>> dataset.as_dict()
#{u'FR': {u'2011': 65342776.0, u'2010': 65027512.0, u'2012': 65659790.0}, u'JP': {u'2011': 127817277.0, u'2010': 128070000.0, u'2012': 127561489.0}, u'GB': {u'2011': 63258918.0, u'2010': 62766365.0, u'2012': 63700300.0}}
#>>> dataset.api_url
#'http://api.worldbank.org/countries/GBR;FRA;JPN/indicators/SP.POP.TOTL?date=2010%3A2012&format=json&per_page=10000'
#>>> dataset.indicator_topics
#[{u'id': u'19', u'value': u'Climate Change'}, {u'id': u'8', u'value': u'Health '}]
#>>> dataset.api_response
#[{u'per_page': u'10000', u'total': 9, u'page': 1, u'pages': 1}, [{u'date': u'2012', u'country': {u'id': u'FR', u'value': u'France'}, u'indicator': {u'id': u'SP.POP.TOTL', u'value': u'Population, total'}, u'decimal': u'0', u'value': u'65659790'}, {u'date': u'2011', u'country': {u'id': u'FR', u'value': u'France'}, u'indicator': {u'id': u'SP.POP.TOTL', u'value': u'Population, total'}, u'decimal': u'0', u'value': u'65342776'}, {u'date': u'2010', u'country': {u'id': u'FR', u'value': u'France'}, u'indicator': {u'id': u'SP.POP.TOTL', u'value': u'Population, total'}, u'decimal': u'0', u'value': u'65027512'}, {u'date': u'2012', u'country': {u'id': u'GB', u'value': u'United Kingdom'}, u'indicator': {u'id': u'SP.POP.TOTL', u'value': u'Population, total'}, u'decimal': u'0', u'value': u'63700300'}, {u'date': u'2011', u'country': {u'id': u'GB', u'value': u'United Kingdom'}, u'indicator': {u'id': u'SP.POP.TOTL', u'value': u'Population, total'}, u'decimal': u'0', u'value': u'63258918'}, {u'date': u'2010', u'country': {u'id': u'GB', u'value': u'United Kingdom'}, u'indicator': {u'id': u'SP.POP.TOTL', u'value': u'Population, total'}, u'decimal': u'0', u'value': u'62766365'}, {u'date': u'2012', u'country': {u'id': u'JP', u'value': u'Japan'}, u'indicator': {u'id': u'SP.POP.TOTL', u'value': u'Population, total'}, u'decimal': u'0', u'value': u'127561489'}, {u'date': u'2011', u'country': {u'id': u'JP', u'value': u'Japan'}, u'indicator': {u'id': u'SP.POP.TOTL', u'value': u'Population, total'}, u'decimal': u'0', u'value': u'127817277'}, {u'date': u'2010', u'country': {u'id': u'JP', u'value': u'Japan'}, u'indicator': {u'id': u'SP.POP.TOTL', u'value': u'Population, total'}, u'decimal': u'0', u'value': u'128070000'}]]
#>>> population_indicators = api.get_indicators(search="population")
#>>> len(population_indicators)
#1280

def list_countries(country_codes=None, search="united", search_full=False):
    api = wbpy.IndicatorAPI()

    countries = api.get_countries(country_codes, search, search_full)
    
    return countries
