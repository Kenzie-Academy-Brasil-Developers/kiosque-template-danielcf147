from statistics import mode
from menu import products

def get_product_by_id(id: int):
    if not type(id) == int:
        raise TypeError("product id must be an int")   

    for element in products:
        if element["_id"] == id:
            return element

    return {}


def get_products_by_type(food_type: str):
    
    if not type(food_type) == str:
        raise TypeError("product type must be a str")

    new_list = []   

    for element in products:
        if element["type"] == food_type:
            new_list.append(element)  
    print(new_list)
    return new_list


def add_product(products, **menu: dict):
    if len(products) > 0:
        menu["_id"] = len(products)+1
        products.append(menu)
    
        return menu

    menu["_id"] = 1
    products.append(menu)
    return menu

def menu_report():
    count_product = 0
    average_price = 0
    most_common_type = []

    for item in products:
            count_product +=1
            average_price += item['price']
            most_common_type.append(item['type'])

    most_common_type_aux = mode(most_common_type)
    average_price_aux = round(average_price/count_product, 2)
    return f"Products Count: {count_product} - Average Price: ${average_price_aux} - Most Common Type: {most_common_type_aux}"



