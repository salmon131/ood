import decimal

class Common:
    @staticmethod
    def calc_amount_including_tax(amount_excluding_tax, tax_rate):
        return amount_excluding_tax * tax_rate
    
    @staticmethod
    def has_resigned(user):
        ...

    @staticmethod
    def create_order(product):
        ...

    @staticmethod
    def is_valid_phone_number(phone_number):
        ...


class TaxRate:
    def __init__(self, value: decimal.Decimal):
        self.value = value


class AmountExcludingTax:
    def __init__(self, value: decimal.Decimal):
        self.value = value

    
class AmountIncludingTax:
    def __init__(self, amount_excluding_tax: AmountExcludingTax, tax_rate: TaxRate):
        self.value = amount_excluding_tax.value * tax_rate.value


if __name__ == "__main__":
    tax_rate = TaxRate(decimal.Decimal("1.1"))
    amount_excluding_tax = AmountExcludingTax(decimal.Decimal("1000"))

    amount_excluding_tax = AmountIncludingTax(amount_excluding_tax, tax_rate)
    print(amount_excluding_tax.value)