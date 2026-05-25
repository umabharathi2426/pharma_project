# ✅ POC1
from sql.create_tables import create_tables
from sql.insert_data import insert_sample_data
from sql.view_data import display_all_tables

# ✅ POC2
from models.sale import Sale
from services.sales_service import SalesService

# ✅ POC3 (ETL)
from etl.extract import extract
from etl.transform import transform
from etl.load import load


def run_project():

    print("\n========================================")
    print("POC1: DATA WAREHOUSING")
    print("========================================")

    print("\n[Step 1] Creating Tables...")
    create_tables()

    print("\n[Step 2] Inserting Sample Data...")
    insert_sample_data()

    print("\n[Step 3] Displaying Tables...")
    display_all_tables()

    # ✅ POC2
    print("\n========================================")
    print("POC2: OOP IMPLEMENTATION")
    print("========================================")

    print("\n[Step 4] Adding Sale using OOP...")

    service = SalesService()
    sale = Sale(medicine_id=1, quantity=2, price=50)
    service.add_sale(sale)

    print("\n[Step 5] Updated Tables:")
    display_all_tables()

    # ✅ ✅ POC3 (THIS IS YOUR STEP 4 UPGRADE ✅)
    print("\n========================================")
    print("POC3: ETL PIPELINE")
    print("========================================")

    print("\n[Step 6] Extracting Data from CSV...")
    med, sup, inv, sales = extract()

    print("\n[Step 7] Transforming Data...")
    med, sup, inv, sales = transform(med, sup, inv, sales)

    print("\n[Step 8] Loading Data into Database...")
    load(med, sup, inv, sales)

    print("\n[Step 9] Final Tables After ETL:")
    display_all_tables()


if __name__ == "__main__":
    run_project()