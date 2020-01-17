"""Classes for melon orders."""
class AbstractMelonOrder():
    """An abstract base class that other Melon Orders inherit from."""
    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.fee = 0 


    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True     


    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5

        if self.species == 'Christmas melons':
            base_price *= 1.5

        # total = (1 + self.tax) * self.qty * base_price
        
        total = (1 + self.tax) * self.qty * base_price + self.fee
        

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




class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    order_type = "international"
    tax = 0.17

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        super().__init__(species, qty)
        self.country_code = country_code
        
        if self.qty < 10:
            self.fee = 3


    def get_country_code(self):
        """Return the country code."""

        return self.country_code

order1 = DomesticMelonOrder('watermelon', 6)
# print(order1.order_type, order1.tax)
print(order1.get_total())

order0 = InternationalMelonOrder("watermelon", 6, "AUS")
print(order0.get_total())
# print(order0.tax, order0.order_type, order0.country_code, order0.qty, order0.species)
