import json

def file_reader(list_name):
    with open (list_name)as file:
        content=json.load(file)
        return content 

def file_writer(list_name, content_to_write):
    with open(list_name, "w")as file:
        json.dump(content_to_write, file, indent=4)  

"""
temp=file_reader("products_list.json")

file_writer("products_list.json", temp)
print(file_reader("products_list.json"))



def print_dic(my_list):
    for i in range(len(my_list)):
        print(my_list[i] , f" : number {i} ")
        my_dic[a]:x+ "\n"
"""


#Products


def products_print():
    with open ("products_list.json")as file:
        products=json.load(file)
        print(products)


def products_create(): 
    products=file_reader("products_list.json")
    print(products)
    new_number=input("new number: ")
    new_product=input("new product: ")
    products[new_product]=int(new_number)
    file_writer("products_list.json", products)
    print(products)

def products_createe(): 
    with open ("products_list.json")as file:
        products=json.load(file)
        print(products)
        new_number=input("new number: ")
        new_product=input("new product: ")
        products[new_product]=int(new_number)
        print(products)
    with open("products_list.json", "w")as file:
        json.dump(products, file, indent=4)


def products_update():
    with open ("products_list.json")as file:
        products=json.load(file)
        print(products)     
        update_number=input("update number: ")
        update_product=input("update product: ")
        products[update_product]=int(update_number)
        previous_product=input("previous product: ")
        del products[previous_product]
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


def couriers_create():
    with open ("couriers_list.json")as file:
        couriers=json.load(file)
        print(couriers)
        new_number=input("new number: ")
        new_courier=input("new courier: ")
        couriers[new_number]=new_courier
        print(couriers)
    with open("couriers_list.json", "w")as file:
        json.dump(couriers, file, indent=4)


def couriers_update():
    with open ("couriers_list.json")as file:
        couriers=json.load(file)
        print(couriers)   
        update_number=input("update number: ")
        update_courier=input("update courier: ")  
        couriers[update_number]=update_courier
        delete_courier=input("previous courier number: ")
        del couriers[delete_courier]
        print(couriers)
    with open("couriers_list.json", "w")as file:
        json.dump(couriers , file, indent=4)


def couriers_delete():
    with open ("couriers_list.json")as file:
        couriers=json.load(file)
        print(couriers)      
        delete_courier=input("delete courier number: ")
        del couriers[delete_courier]
        print(couriers)
    with open("couriers_list.json", "w")as file:
        json.dump(couriers, file, indent=4)


#orders


def print_list(my_list):
    for i in range(len(my_list)):
        print(my_list[i] , f" : number {i} ")


def orders_print():
    with open ("orders_list.json")as file:
        orders=json.load(file)
        print_list(orders)


def orders_create():
    with open ("orders_list.json")as file:
        orders=json.load(file)
        print_list(orders)
        with open ("couriers_list.json")as file:
            couriers=json.load(file)
        customername=input("customer_name:")
        customeraddress=input("customer_address:")
        customerphon=input("customer_phone:")
        print(couriers)
        customercourier=couriers[input("courier nimber:")]
        customerstatus="preparing"
        neworder={"customer_name":customername,
        "customer_address":customeraddress,
        "customer_phone":customerphon,
        "courier":customercourier,
        "status":customerstatus }
        orders.append(neworder)
        print_list(orders)
    with open("orders_list.json", "w")as file:
        json.dump(orders, file, indent=4)



status=["preparing", "sending", "delivered"]
def orders_update_status():
    with open ("orders_list.json")as file:
        orders=json.load(file)
        print_list(orders)
        status_index=int(input("preparing(0), sending(1), delivered(2):"))
        status=int(input("order number:"))
        status[status_index]=orders[status]["status"]
        print_list(orders)
    with open("orders_list.json", "w")as file:
        json.dump(orders, file, indent=4)


def orders_update_order():
    with open ("orders_list.json")as file:
        orders=json.load(file)
        print_list(orders)
        order_number=int(input("order number:"))
        new_name=input("customer_name:")
        if new_name != "":  
            orders[order_number]["customer_name"]=new_name
        new_address=input("customer_address:")
        if new_address != "":
            orders[order_number]["customer_address"]=new_address
        new_phone=input("customer_phone:")
        if new_phone != "":
            orders[order_number]["customer_phone"]=new_phone
        print_list(orders)
    with open("orders_list.json", "w")as file:
        json.dump(orders, file, indent=4)



def orders_delete():
    with open ("orders_list.json")as file:
        orders=json.load(file)
        print_list(orders)
        delete_order=int(input("delete order number: "))
        del orders[delete_order]
        print_list(orders)
    with open("orders_list.json", "w")as file:
        json.dump(orders, file, indent=4)

