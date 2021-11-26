import requests

""" Get data """
url = "https://www.cnb.cz/cs/financni_trhy/devizovy_trh/kurzy_devizoveho_trhu/denni_kurz.txt"
req = requests.get(url)

if not req.ok:
    raise Exception("Request failed")

""" Parse into lines """

response = req.text
lines = response.splitlines()


""" Ignore first two lines """
_info = lines.pop(0)
_table_header = lines.pop(0)

""" Add input for czk """
lines.append("Ceska Republika|ceska koruna|1|CZK|1")


class ExchangeRate():
    """ Class for keeping Exchange Rate for each country"""

    def __init__(self, line: str):

        country_name, currency, amount, currency_code, rate \
            = line.split("|")

        self._country_name = country_name
        self._currency = currency
        self._currency_code = currency_code
        self._rate = float(rate.replace(",", ".")) / \
            float(amount.replace(",", "."))

    def __str__(self):
        return "1 CZK = {} {}".format(
            self._currency_code,
            self._rate)

    def convertToCZK(self, amount: float) -> float:
        print("Convert {} {} into CZK with rate {}".format(
            amount, self._currency_code, self._rate
        ))

        return amount * self._rate

    def convertFromCZK(self, amount: float) -> float:
        print("Convert {} CZK into {} with rate {}".format(
            amount, self._currency_code, self._rate
        ))
        return amount / self._rate

    # def convert(self, amount, )


rates = [ExchangeRate(line) for line in lines]


def echange(amount: float, source_currency: str, target_currency: str) -> float:
    """ 
    ``` 
    x = echange(100, "CAD", "EUR") 
    ``` 
    """
    source_currency = source_currency.upper()
    target_currency = target_currency.upper()

    source_rate = list(filter(lambda rate: rate._currency_code ==
                              source_currency, rates))[0]

    print(source_rate)

    target_rate = list(filter(lambda rate: rate._currency_code ==
                              target_currency, rates))[0]

    print(target_rate)

    amount_in_czk = source_rate.convertToCZK(amount)

    print(amount_in_czk)

    result = target_rate.convertFromCZK(amount_in_czk)

    return result
