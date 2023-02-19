import json
import random

def file_reader(list_name):
    with open (list_name)as file:
        content=json.load(file)
        return content 


def file_writer(list_name, content_to_write):
    with open(list_name, "w")as file:
        json.dump(content_to_write, file, indent=4)  


#Products

def code_products():
    products=file_reader("products_list.json")
    for i in range(len(products)):
            y=random.randint(1,100)
            while True:
                codenumbers=products[i]["code"]
                if y== codenumbers :
                    y=random.randint(1,100)
                else: return y


def products_print():
    products=file_reader("products_list.json")
    for i in range(len(products)):
        num=f"product number: {i} \n"
        productcode=products[i]["code"]
        code=f"code:  {productcode} \n"
        productname=products[i]["name"]
        name=f"name:  {productname} \n"
        productprice=products[i]["price"]
        price=f"price:  {productprice} \n"
        print("\n"+num+code+name+price)
            

def products_create(): 
    products=file_reader("products_list.json")
    products_print()
    new_name=input("new name: ")
    new_price=input("new price: ")
    newproduct={ "code":code_products(), "name":new_name, "price":new_price}
    products.append(newproduct)
    file_writer("products_list.json", products)
    products_print()


def products_update():
    products=file_reader("products_list.json")
    products_print()  
    product_number=int(input("product number:"))
    new_name=input("product name:")
    if new_name != "":  
        products[product_number]["name"]=new_name
    new_price=input("product price:")
    if new_price != "":
        products[product_number]["price"]=new_price
    file_writer("products_list.json", products)
    products_print()


def products_delete():
    products=file_reader("products_list.json")
    products_print()      
    delete_product=int(input("delete product number: "))
    del products[delete_product]
    file_writer("products_list.json", products)
    products_print()


#Couriers

def code_couriers():
    couriers=file_reader("couriers_list.json")
    for i in range(len(couriers)):
            y=random.randint(1,100)
            while True:
                codenumbers=couriers[i]["code"]
                if y== codenumbers :
                    y=random.randint(1,100)
                else: return y


def couriers_print():
    couriers=file_reader("couriers_list.json")
    for i in range(len(couriers)):
        num=f"courier number: {i} \n"
        couriercode=couriers[i]["code"]
        code=f"code:  {couriercode} \n"
        couriername=couriers[i]["name"]
        name=f"name:  {couriername} \n"
        courierphone=couriers[i]["phone"]
        price=f"phone:  {courierphone} \n"
        print("\n"+num+code+name+price)


def couriers_create():
    couriers=file_reader("couriers_list.json")
    couriers_print()
    new_name=input("new name: ")
    new_phone=input("new phone: ")
    newcourier={"code":code_couriers(),"name":new_name, "phone":new_phone}
    couriers.append(newcourier)
    file_writer("couriers_list.json", couriers)
    couriers_print()


def couriers_update():
    couriers=file_reader("couriers_list.json")
    couriers_print()   
    courier_number=int(input("courier number:"))
    new_name=input("courier name:")
    if new_name != "":  
        couriers[courier_number]["name"]=new_name
    new_phone=input("courier phone:")
    if new_phone != "":
        couriers[courier_number]["phone"]=new_phone
    file_writer("couriers_list.json", couriers)
    couriers_print()


def couriers_delete():
    couriers=file_reader("couriers_list.json")
    couriers_print()      
    delete_courier=int(input("delete courier number: "))
    del couriers[delete_courier]
    file_writer("couriers_list.json", couriers)
    couriers_print()


#orders

def code_orders():
    orders=file_reader("orders_list.json")
    for i in range(len(orders)):
            y=random.randint(1,100)
            while True:
                codenumbers=orders[i]["code"]
                if y== codenumbers :
                    y=random.randint(1,100)
                else: return y


def orders_print():
    orders=file_reader("orders_list.json")
    for i in range(len(orders)):
        num=f"customer number: {i} \n"
        ordercode=orders[i]["code"]
        a=f"code:  {ordercode} \n"
        ordercustomername=orders[i]["customer_name"]
        b=f"customer_name:  {ordercustomername} \n"
        ordercustomeraddress=orders[i]["customer_address"]
        c=f"customer_address:  {ordercustomeraddress} \n"
        ordercustomerphone=orders[i]["customer_phone"]
        d=f"customer_phone:  {ordercustomerphone} \n"
        ordercourier=orders[i]["courier"]
        e=f"courier:  {ordercourier} \n"
        orderstatus=orders[i]["status"]
        f=f"status:  {orderstatus} \n"
        orderitems=orders[i]["items"]
        g=f"items:  {orderitems} \n"
        print(num+a+b+c+d+e+f+g) 


def orders_create():
    orders=file_reader("orders_list.json")
    orders_print()
    couriers=file_reader("couriers_list.json")
    customername=input("customer_name:")
    customeraddress=input("customer_address:")
    customerphon=input("customer_phone:")
    products_print()
    items = [int(x) for x in input("product code with space:").split()]
    couriers_print()
    customercourier=int(input("courier code:"))
    customerstatus="preparing"
    neworder={"code":code_orders(),
    "customer_name":customername,
    "customer_address":customeraddress,
    "customer_phone":customerphon,
    "courier":customercourier,
    "status":customerstatus,
    "items":items }
    orders.append(neworder)
    file_writer("orders_list.json",orders)
    orders_print()


status=["preparing", "sending", "delivered"]
def orders_update_status():
    orders=file_reader("orders_list.json")
    orders_print()
    status_index=int(input("preparing(0), sending(1), delivered(2):"))
    status=int(input("order number:"))
    status[status_index]=orders[status]["status"]
    file_writer("orders_list.json", orders)
    orders_print()


def orders_update_order():
    orders=file_reader("orders_list.json")
    orders_print()
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
    orders_print()


def orders_delete():
    orders=file_reader("orders_list.json")
    orders_print()
    delete_order=int(input("delete order number: "))
    del orders[delete_order]
    file_writer("orders_list.json", orders)
    orders_print()


