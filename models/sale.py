class Sale:
    def __init__(self, medicine_id, quantity, price):
        self.medicine_id = medicine_id
        self.quantity = quantity
        self.price = price

    def calculate_total(self):
        return self.quantity * self.price
