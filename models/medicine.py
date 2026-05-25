class Medicine:
    def __init__(self, medicine_id, name, category, price):
        self.medicine_id = medicine_id
        self.name = name
        self.category = category
        self.price = price

    def __str__(self):
        return f"{self.name} - {self.category} - ₹{self.price}"