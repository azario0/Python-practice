"""
lets say you have a function called convert currency has 3 inputs. 1  has list of currencies and conversion rates,  2 starting currency and ending currency `convert_currency([conversion_rates], start_currency, end_currency)`.
in the list of currencies you have 3 values, start, end, conversion  rate from start to end currency ->  `conversion_rate = [start,end,rate]`. for example ["USD","GBP",0.77]. 
give the above Parameters find the conversion rate from the starting to the end currency the returned value should be a number.
"""
def conversion_rate(conversion_rates, start_currency, end_currency):
    for conversion_rate in conversion_rates:
        if conversion_rate[0] == start_currency and conversion_rate[1] == end_currency:
            return conversion_rate[2]
    return None #return None if no conversion rate is found

def convert_currency(conversion_rates, start_currency, end_currency):
    #get the conversion rate
    rate = conversion_rate(conversion_rates, start_currency, end_currency)
    #if the rate is None, return None
    if rate == None:
        return None
    # else:
    #     raise ValueError("Conversion rate not found for the given currencies.")
    #otherwise, return the conversion
    return rate * 100


def test_convert_currency():
    conversion_rates = [("USD", "EUR", 0.85), ("EUR", "JPY", 129.52), ("USD", "JPY", 109.57)]
    assert convert_currency(conversion_rates, "USD", "EUR") == 0.85 * 100
    assert convert_currency(conversion_rates, "EUR", "JPY") == 129.52 * 100
    assert convert_currency(conversion_rates, "USD", "JPY") == 109.57 * 100
    assert convert_currency(conversion_rates, "JPY", "USD") == None
## Example
conversion_rates = [("USD", "EUR", 0.85), ("EUR", "JPY", 129.52), ("USD", "JPY", 109.57)]
start_currency = "USD"
end_currency = "EUR"
print(convert_currency(conversion_rates, start_currency, end_currency))