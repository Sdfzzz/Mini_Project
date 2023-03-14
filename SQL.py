import pymysql.cursors
import os
from dotenv import load_dotenv
from database import *

load_dotenv(".env")

HOST=os.environ.get("HOST")
USER_NAME=os.environ.get("USER_NAME")
PASSWORD=os.environ.get("PASSWORD")
DATABASE=os.environ.get("DATABASE")


connection = pymysql.connect(host=HOST,
                            user=USER_NAME,
                            password=PASSWORD,
                            database=DATABASE,
                            cursorclass=pymysql.cursors.DictCursor)

cursor=connection.cursor()


def read_database(query):
    cursor.execute(query)
    result=cursor.fetchall()
    return result


def write_database(query):
    cursor.execute(query)
    result=cursor.fetchall()
    connection.commit()
    return result

def close_database():
    cursor.close()
    connection.close()


def initialize_db():
    write_database(products_db)
    write_database(couriers_db)
    write_database(customers_db)
    write_database(orders_db)
    write_database(productorders_db)


def beverage_count():
    result=read_database("select  po.product_ID from productorders po")
    z=0
    for i in range(len(result)):
        x=result[i]["product_ID"]
        if x==3:
            z=z+1
        elif x==4:
            z=z+1    
    return z

def meal_count():
    result=read_database("select  po.product_ID from productorders po")
    z=0
    for i in range(len(result)):
        x=result[i]["product_ID"]
        if x==1:
            z=z+1
        elif x==2:
            z=z+1    
    return z


beverage_order=beverage_count()
meal_order=meal_count()



#products


def products_print():
    select_all="SELECT ID, name, price FROM products"
    result=read_database(select_all)
    for i in range(len(result)):
        resultt=f"{result[i]}\n"
        print(resultt) 
              
 
def products_create():
    products_print()
    new_name=input("new name: ")
    new_price=input("new price: ")
    result=f"INSERT into products ( name, price) values ( '{new_name}', {new_price})"
    write_database(result)
    products_print()
            

def products_update():
    products_print()
    product_ID=int(input("product ID: "))
    new_name=input("product name: ")
    new_price=input("product price: ")
    result1=f"UPDATE products SET  name='{new_name}' WHERE ID={product_ID}"
    result2=f"UPDATE products SET price={new_price}  WHERE ID={product_ID}"
    if new_name !="" and new_price=="":  
        write_database(result1)
    if new_price !="" and new_name=="":     
        write_database(result2)
    if new_name !="" and new_price !="":
        write_database(result1)
        write_database(result2)
    products_print()
            

def products_delete():
    products_print()
    product_ID=int(input("product ID: "))
    result=f"DELETE FROM products WHERE ID={product_ID}"
    write_database(result)
    products_print()
     

#couriers


def couriers_print():
    select_all="SELECT ID, name, phone FROM couriers"
    result=read_database(select_all)
    for i in range(len(result)):
        resultt=f"{result[i]}\n"
        print(resultt) 


def couriers_create():
    couriers_print()
    new_name=input("new name: ")
    new_phone=input("new phone: ")
    result=f"INSERT into couriers ( name, phone) values ( '{new_name}', {new_phone})"
    write_database(result)  
    couriers_print()


def couriers_update():
    couriers_print()   
    courier_ID=int(input("courier ID: "))
    new_name=input("courier name: ")
    new_phone=input("courier phone: ")
    result1=f"UPDATE couriers SET  name='{new_name}' WHERE ID={courier_ID}"
    result2=f"UPDATE couriers SET phone={new_phone}  WHERE ID={courier_ID}"
    if new_name !="" and new_phone=="":  
        write_database(result1)
    elif new_phone !="" and new_name=="":     
        write_database(result2)
    elif new_name !="" and new_phone !="":
        write_database(result1)
        write_database(result2)    
    couriers_print()


def couriers_delete():
    couriers_print()
    courier_ID=int(input("courier ID: "))
    result=f"DELETE FROM couriers WHERE ID={courier_ID}"
    write_database(result)
    couriers_print()
    

#customers


def customers_print():
    select_all="SELECT ID, customer_name, customer_address, customer_phone FROM customers"
    result=read_database(select_all)
    for i in range(len(result)):
        resultt=f"{result[i]}\n"
        print(resultt) 


def customers_create():
    customers_print()
    customername=input("customer_name: ")
    customeraddress=input("customer_address: ")
    customerphone=input("customer_phone: ")
    result=f"""INSERT into customers ( customer_name, customer_address, customer_phone) 
    values ( '{customername}', '{customeraddress}','{customerphone}')"""
    write_database(result)  
    customers_print()


def customers_update():
    customers_print()   
    customer_ID=int(input("customer ID: "))
    customername=input("customer_name: ")
    if customername !="":
        result=f"UPDATE customers SET  customer_name='{customername}' WHERE ID={customer_ID}"
        write_database(result)
    customeraddress=input("customer_address: ")
    if customeraddress !="":
        result=f"UPDATE customers SET customer_address={customeraddress}  WHERE ID={customer_ID}"
        write_database(result)
    customerphone=input("customer_phone: ")
    if customerphone !="":
        result=f"UPDATE customers SET customer_phone={customerphone}  WHERE ID={customer_ID}"
        write_database(result)    
    customers_print()


def customers_delete():
    customers_print()
    customer_ID=int(input("customer ID: "))
    result=f"DELETE FROM customers WHERE ID={customer_ID}"
    write_database(result)
    customers_print()

#orders

def productorders_print():
    select_all="SELECT order_ID, product_ID  FROM productorders"
    result=read_database(select_all)
    for i in range(len(result)):
        x=result[i]["order_ID"]
        y=result[i]["product_ID"]
        z=result[i-1]["order_ID"]
        if x !=z:
            print(f"\norder ID: {x}")
        print(y)
       

def ordertotal_print():
    select_all="""select
    o.ID ,
    c.name, 
    p.name ,
    cu.customer_phone
    from orders o 
    join productorders po on o.ID =po.order_ID 
    join customers cu on cu.ID =o.customer_ID  
    join products p on po.product_ID =p.ID 
    join couriers c on o.courier_ID =c.ID"""
    result=read_database(select_all)
    for i in range(len(result)):
        x=result[i]["ID"]
        y=result[i]["p.name"]
        z=result[i-1]["ID"]
        a=result[i]["name"]
        b=result[i]["customer_phone"]
        if x !=z:
            print(f"\norder ID: {x}\ncorier name: {a}\ncustomer number: {b}")
        print(y)
    

def orders_print():
    select_all="SELECT ID, customer_ID, courier_ID, status, product_ID  FROM orders"
    result=read_database(select_all)
    for i in range(len(result)):
        resultt=f"{result[i]}\n"
        print(resultt)  


def orders_create():
    orders_print()
    customers_print()
    customerID=int(input("customer_ID: "))
    products_print()
    customerproduct=[int(x) for x in input("product ID with space: ").split()]
    couriers_print()
    customercourier=int(input("courier_ID: "))
    result=f"""INSERT into orders (customer_ID, courier_ID, status, product_ID) 
    values ('{customerID}', '{customercourier}', 'preparing', '{customerproduct}')"""
    write_database(result)
    orders_print()
    select_orderID="SELECT ID FROM orders "
    orderID=read_database(select_orderID)
    orderIDselection=orderID[-1]["ID"]
    for i in customerproduct:
        resultt=f"INSERT into productorders (order_ID, product_ID) values ('{orderIDselection}', '{i}')  "
        write_database(resultt)


status=["preparing", "sending", "delivered"]
def orders_update_status():
    orders_print()
    order_ID=int(input("order_ID:"))
    status_index=int(input("preparing(1), sending(2), delivered(3):"))
    if status_index==1:
        statusorder="preparing"
    elif status_index==2:
        statusorder="sending"
    elif status_index==3:
        statusorder="delivered"    
    result=f"UPDATE orders SET  status='{statusorder}' WHERE ID={order_ID}"
    write_database(result)
    orders_print()


def orders_update_order():
    orders_print()
    order_ID=int(input("order number:"))
    new_customer=input("new customer_ID: ")  
    if new_customer !="":
        result=f"UPDATE orders SET  customer_ID='{new_customer}' WHERE ID={order_ID}"
        write_database(result)     
    products_print()
    new_product=[int(x) for x in input("product ID with space:").split()]
    if new_product !="":
        result=f"UPDATE orders SET  product_ID='{new_product}' WHERE ID={order_ID}"        
        write_database(result)  
        resultt=f"DELETE FROM productorders WHERE order_ID={order_ID}"
        write_database(resultt)
        for i in new_product:
            resultt=f"INSERT into productorders (order_ID, product_ID) values ('{order_ID}', '{i}')  "
            write_database(resultt)        
    couriers_print()    
    new_courier=input("new courier_ID: ")  
    if new_courier !="":
        result=f"UPDATE orders SET  courier_ID='{new_courier}' WHERE ID={order_ID}"        
        write_database(result)
    orders_print()


def orders_delete():
    orders_print()
    order_ID=int(input("order ID: "))
    result=f"DELETE FROM orders WHERE ID={order_ID}"
    write_database(result)   
    resultt=f"DELETE FROM productorders WHERE order_ID={order_ID}"
    write_database(resultt) 
    orders_print()
