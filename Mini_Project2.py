
import json
from functions import products_print, products_create, products_update, products_delete
from functions import couriers_print, couriers_create, couriers_update,couriers_delete


product_menu_option=["returne", "print", "create", "update", "delete"]
courier_menu_option=["returne", "print", "create", "update", "delete"]


while True:
    inputt=int(input("exit(0) , product_menu_option(1) , courier_menu_option(2): "))

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

    elif inputt ==2:
        print(courier_menu_option)
        with open ("couriers_list.json", "r")as file:
            couriers=file.read()
        while True:
            input_user2=int(input("return(o), print(1), create(2), update(3) or delete(4): "))
            if input_user2 == 0:
                break
            elif input_user2 == 1  :
                couriers_print()
            elif input_user2 == 2  :
                couriers_create
            elif input_user2 == 3  :
                couriers_update
            elif input_user2 == 4  :
                couriers_delete