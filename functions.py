import json


def file_reader(list_name):
    with open (list_name)as file:
        content=json.load(file)
        return content 

def file_writer(list_name, content_to_write):
    with open(list_name, "w")as file:
        json.dump(content_to_write, file, indent=4)  



#Products


def products_print():
    products=file_reader("products_list.json")
    print(products)


def products_create(): 
    products=file_reader("products_list.json")
    print(products)
    new_number=input("new number: ")
    new_product=input("new product: ")
    products[new_product]=int(new_number)
    file_writer("products_list.json", products)
    print(products)


def products_update():
    products=file_reader("products_list.json")
    print(products)    
    update_number=input("update number: ")
    update_product=input("update product: ")
    products[update_product]=int(update_number)
    previous_product=input("previous product: ")
    del products[previous_product]
    file_writer("products_list.json", products)
    print(products)


def products_delete():
    products=file_reader("products_list.json")
    print(products)      
    delete_product=input("delete product: ")
    del products[delete_product]
    file_writer("products_list.json", products)
    print(products)


#Couriers

def couriers_print():
    couriers=file_reader("couriers_list.json")
    print(couriers)


def couriers_create():
    couriers=file_reader("couriers_list.json")
    print(couriers)
    new_number=input("new number: ")
    new_courier=input("new courier: ")
    couriers[new_number]=new_courier
    print(couriers)
    file_writer("couriers_list.json", couriers)
    print(couriers)


def couriers_update():
    couriers=file_reader("couriers_list.json")
    print(couriers)   
    update_number=input("update number: ")
    update_courier=input("update courier: ")  
    couriers[update_number]=update_courier
    delete_courier=input("previous courier number: ")
    del couriers[delete_courier]
    print(couriers)
    file_writer("couriers_list.json", couriers)
    print(couriers)


def couriers_delete():
    couriers=file_reader("couriers_list.json")
    print(couriers)      
    delete_courier=input("delete courier number: ")
    del couriers[delete_courier]
    print(couriers)
    file_writer("couriers_list.json", couriers)
    print(couriers)


#orders


def print_list(my_list):
    for i in range(len(my_list)):
        print(my_list[i] , f" : number {i} ")


def orders_print():
    orders=file_reader("orders_list.json")
    print_list(orders)


def orders_create():
    orders=file_reader("orders_list.json")
    print_list(orders)
    couriers=file_reader("couriers_list.json")
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
    file_writer("orders_list.json",orders)
    print_list(orders)
    



status=["preparing", "sending", "delivered"]
def orders_update_status():
    orders=file_reader("orders_list.json")
    print_list(orders)
    status_index=int(input("preparing(0), sending(1), delivered(2):"))
    status=int(input("order number:"))
    status[status_index]=orders[status]["status"]
    file_writer("orders_list.json", orders)
    print_list(orders)


def orders_update_order():
    orders=file_reader("orders_list.json")
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
    file_writer("orders_list.json", orders)
    print_list(orders)




def orders_delete():
    orders=file_reader("orders_list.json")
    print_list(orders)
    delete_order=int(input("delete order number: "))
    del orders[delete_order]
    file_writer("orders_list.json", orders)
    print_list(orders)


