from SQL import * 

product_menu_option=["return", "print", "create", "update", "delete"]
courier_menu_option=["return", "print", "create", "update", "delete"]
customer_menu_option=["return", "print", "create", "update", "delete"]
order_menu_option=["return", "print", "create", "update status", "update order", "delete"]
productorder_menu_option=["return", "print product order", "print total order"]

menu="""exit(0)
product_menu_option(1)
courier_menu_option(2)
customer_menu_option(3)
order_menu_option(4)
productorder_menu_option(5): """


def all():
    inputt=int(input(menu))

    if inputt == 0:
        exit()

    elif inputt==1:
        print(product_menu_option)
        while True:
            input_user=int(input("return(o), print(1), create(2), update(3) or delete(4): "))
            if input_user == 0:
                break
            elif input_user == 1  :
                products_print()
            elif input_user == 2  :
                products_create()
            elif input_user == 3  :
                products_update()
            elif input_user == 4  :
                products_delete()
            else:
                print("Wrong input \nTry again")    

    elif inputt ==2:
        print(courier_menu_option)
        while True:
            input_user2=int(input("return(o), print(1), create(2), update(3) or delete(4): "))
            if input_user2 == 0:
                break
            elif input_user2 == 1  :
                customers_print()
            elif input_user2 == 2  :
                customers_create()
            elif input_user2 == 3  :
                customers_update()
            elif input_user2 == 4  :
                customers_delete()
            else:
                print("Wrong input \nTry again")    

    elif inputt ==3:
        print(customer_menu_option)
        while True:
            input_user3=int(input("return(o), print(1), create(2), update(3) or delete(4): "))
            if input_user3 == 0:
                break
            elif input_user3 == 1  :
                couriers_print()
            elif input_user3 == 2  :
                couriers_create()
            elif input_user3 == 3  :
                couriers_update()
            elif input_user3 == 4  :
                couriers_delete()  
            else:
                print("Wrong input \nTry again")              
    
    elif inputt ==4:
        print(order_menu_option)
        while True:
            input_user4=int(input("return(o), print(1), create(2), update status(3), update order(4) or delete(5): "))
            if input_user4 == 0:
                break
            elif input_user4 == 1  :
                orders_print()
            elif input_user4 == 2  :
                orders_create()
            elif input_user4 == 3  :
                orders_update_status()
            elif input_user4 == 4  :
                orders_update_order()
            elif input_user4 == 5  :
                orders_delete()
            else:
                print("Wrong input \nTry again")    

    elif inputt==5:
        print(productorder_menu_option)
        while True:
            input_user5=int(input("return(o), print(1), print total order(2): "))
            if input_user5 == 0:
                break
            elif input_user5 == 1  :
                orders_print()
            elif input_user5 == 2  :
                ordertotal_print()    
            else:
                print("Wrong input \nTry again")   

    all()             
all()        
            