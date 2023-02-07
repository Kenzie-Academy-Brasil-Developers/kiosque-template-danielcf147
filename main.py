from management import product_handler, tab_handler
# from management.product_handler import add_product
if __name__ == "__main__":
    # Seus prints de teste aqui
    print(product_handler.get_product_by_id(25))

    print(product_handler.get_products_by_type("drink"))

    test = {
            "title": "Bolinho JS",
            "price": 1.0,
            "rating": 2,
            "description": "Bolinho de JS com cenoura",
            "type": "bakery"}

    print(product_handler.add_product(**test))

    print(tab_handler.calculate_tab([
                    {"_id": 10, "amount": 3},
                    {"_id": 20, "amount": 2},
                    {"_id": 21, "amount": 5},
                ]))
                
    print(product_handler.menu_report())
    ...
