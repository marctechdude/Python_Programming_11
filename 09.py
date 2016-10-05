currencies = {
    'Canadian Dollar' : 'CAD',
    'United States Dollar' : 'USD',
    'Australian Dollar' : 'AUD',
    'British Pound' : 'GBP',
    'Euro' : 'EUR',
    'Japanese Yen' : 'JPY',
    'Swiss Franc' : 'CHF',
    'Afghanistan Afghani' : 'AFN',
    'Albanian Lek' : 'ALL',
    'Algerian Dinar' : 'DZD',
    'Angolan Kwanza' : 'AOA',
    'Argentine Peso' : 'ARS',
    'Armenian Dram' : 'AMD',
    'Aruban Florin' : 'AWG',
}

for i,j in sorted(currencies.items()):
    print("'%s' is abbreviated to '%s'" % (i,j))

print("-" * 10)

currencies['Canadian Provinces'] = ['BC', 'ON']
# there's a better way to do this but I forgot how, so i just used a constructor
currencies.__delitem__('Afghanistan Afghani')

for i,j in sorted(currencies.items()):
    sorted(currencies)
    print("'%s' is abbreviated to '%s'" % (i,j))