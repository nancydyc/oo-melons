"""Classes for melon orders."""
class AbstractMelonOrder():
    """An abstract base class that other Melon Orders inherit from."""
    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False      


    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True     


    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5
        total = (1 + self.tax) * self.qty * base_price

        return total
   

class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    order_type = "domestic"
    tax = 0.08

    # def __init__(self, species, qty):
    #     """Initialize melon order attributes."""
    #     super().__init__(species, qty)

    #     self.order_type = 'domestic'
    #     self.tax = 0.08

order1 = DomesticMelonOrder('watermelon', 6)
# print(order1.order_type, order1.tax)
print(order1.get_total())


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        super().__init__(species, qty)
        self.country_code = country_code
        self.order_type = "international"
        self.tax = 0.17


    def get_country_code(self):
        """Return the country code."""

        return self.country_code

order0 = InternationalMelonOrder("watermelon", 6, "AUS")
print(order0.tax, order0.order_type, order0.country_code, order0.qty, order0.species)
