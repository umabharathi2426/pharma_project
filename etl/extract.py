import pandas as pd

def extract():
    medicines = pd.read_csv("data/medicines.csv")
    suppliers = pd.read_csv("data/suppliers.csv")
    inventory = pd.read_csv("data/inventory.csv")
    sales = pd.read_csv("data/sales.csv", on_bad_lines='skip')

    print("✅ Data Extracted")

    return medicines, suppliers, inventory, sales

