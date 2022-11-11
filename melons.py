"""Classes for melon orders."""

class AbtractMelonOrder:

    def __init__(self, species, qty, shipped, order_type, tax):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = shipped
        self.order_type = order_type
        self.tax = tax

    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5
        total = (1 + self.tax) * self.qty * base_price

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder(AbtractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        super().__init__(species = species, qty = qty, shipped = False, 
        order_type = "Domestic", tax = 0.08)


    def get_total(self): 
        """Calculate price, including tax.""" 

        base_price = 5 

        if self.species == 'Christmas': 
            new_price = base_price * 1.5
            total = (1 + self.tax) * self.qty * new_price
            return total
        else: 
            return super().get_total()
            

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class InternationalMelonOrder(AbtractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""

        super().__init__(species = species, qty = qty, shipped = False, order_type = "International", tax = 0.17)

        self.country_code = country_code 
        
    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5

        if self.order_type == 'International' and self.qty < 10 and self.species == 'Christmas':
            new_price = (base_price * 1.5) + 3 
            total = (1 + self.tax) * self.qty * new_price
            return total
        elif self.species == 'Christmas':
            new_price = base_price * 1.5
            total = (1 + self.tax) * self.qty * new_price
            return total
        elif self.order_type == 'International' and self.qty < 10:
            new_price = base_price + 3
            total = (1 + self.tax) * self.qty * new_price
            return total
        else:
            return super().get_total()
        

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

    def get_country_code(self):
        """Return the country code."""

        return self.country_code


class GovernmentMelonOrder(AbtractMelonOrder):
    '''Government Melon Orders'''

    def __init__(self, species, qty):

        super().__init__(species = species, qty = qty, shipped = False, 
        order_type = 'Government', tax = 0.00)

        self.passed_inspection = False 
    
    def mark_inspection(self):
        '''Whether or not a melon has passed inspection'''

        if input('Passed?') == 'Passed' or 'passed':
            self.passed_inspection = True
        else:
            self.passed_inspection = False 

