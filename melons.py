"""Classes for melon orders."""

from random import choice
import datetime

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


    def get_base_price(self):

        self.base_price = choice(range(5, 10))
        # self.base_price = 5

        current_time = datetime.datetime.now()
        current_day = current_time.weekday()
        current_hour = current_time.hour

        if current_day in range(1, 6) and current_hour in range(8, 12):
        # if current_day in range(1, 6) and current_hour in range(8, 17):
            self.base_price += 4




    def get_total(self):
        """Calculate price, including tax."""

        self.get_base_price()

        if self.species == 'Christmas melons':
            self.base_price *= 1.5

        # total = (1 + self.tax) * self.qty * base_price
        
        total = (1 + self.tax) * self.qty * self.base_price + self.fee

        return round(total, 2)
   



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


class GovernmentMelonOrder(AbstractMelonOrder):
    tax = 0
    passed_inspection = False

    def mark_inspection(self, passed):
        if passed:
        # if passed:
            self.passed_inspection = passed
            # self.passed_inspection = True

            # return self.passed_inspection
        self.passed_inspection
        # return self.passed_inspection

order1 = DomesticMelonOrder('watermelon', 10)
# print(order1.order_type, order1.tax)

print(order1.get_total())



# order1 = DomesticMelonOrder('watermelon', 6)
# print(order1.order_type, order1.tax)
# print(order1.get_total())

# order0 = InternationalMelonOrder("watermelon", 6, "AUS")
# print(order0.get_total())
# # print(order0.tax, order0.order_type, order0.country_code, order0.qty, order0.species)

# order2 = GovernmentMelonOrder('watermelon', 6)
# # print(order2.mark_inspection(False))
# print(order2.passed_inspection)

# # print(order2.mark_inspection(True))
# print(order2.passed_inspection)
