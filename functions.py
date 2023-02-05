import json


#Products

def products_print():
    with open ("products_list.json")as file:
        products=json.load(file)
        print(products)
    with open("products_list.json", "w")as file:
        json.dump(products, file, indent=4)

   
def products_create():
    with open ("products_list.json")as file:
        products=json.load(file)
        print(products)
        products[input("new product: ")]=int(input("new number: "))
        print(products)
    with open("products_list.json", "w")as file:
        json.dump(products, file, indent=4)


def products_update():
    with open ("products_list.json")as file:
        products=json.load(file)
        print(products)       
        products[input("update product: ")]=int(input("update number: "))
        update_product=input("previous product: ")
        del products[update_product]
        print(products)
    with open("products_list.json", "w")as file:
        json.dump(products, file, indent=4)


def products_delete():
    with open ("products_list.json")as file:
        products=json.load(file)
        print(products)      
        delete_product=input("delete product: ")
        del products[delete_product]
        print(products)
    with open("products_list.json", "w")as file:
        json.dump(products, file, indent=4)


#Couriers

def couriers_print():
    with open ("couriers_list.json")as file:
        couriers=json.load(file)
        print(couriers)
    with open("couriers_list.json", "w")as file:
        json.dump(couriers, file, indent=4)

   
def couriers_create():
    with open ("couriers_list.json")as file:
        couriers=json.load(file)
        print(couriers)
        couriers[input("new courier: ")]=int(input("new number: "))
        print(couriers)
    with open("couriers_list.json", "w")as file:
        json.dump(couriers, file, indent=4)


def couriers_update():
    with open ("couriers_list.json")as file:
        couriers=json.load(file)
        print(couriers)       
        couriers[input("update courier: ")]=int(input("update number: "))
        update_product=input("previous courier: ")
        del couriers[update_product]
        print(couriers)
    with open("couriers_list.json", "w")as file:
        json.dump(couriers , file, indent=4)


def couriers_delete():
    with open ("couriers_list.json")as file:
        couriers=json.load(file)
        print(couriers)      
        delete_product=input("delete courier: ")
        del couriers[delete_product]
        print(couriers)
    with open("couriers_list.json", "w")as file:
        json.dump(couriers, file, indent=4)




        


