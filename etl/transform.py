def transform(med, sup, inv, sales):

    # Sales transformation
    sales["total_price"] = sales["quantity"] * sales["price"]

    print("✅ Data Transformed")

    return med, sup, inv, sales

