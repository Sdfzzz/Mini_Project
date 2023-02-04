
from functions  import print_list

product_menu_option=["returne", "print", "create", "update", "delete"]
courier_menu_option=["returne", "print", "create", "update", "delete"]



while True:
    inputt=int(input("exit(0) , product_menu_option(1) , courier_menu_option(2): "))
    if inputt == 0:
        exit()


    elif inputt==1:
        print(product_menu_option)
        products_list = ["Pizza" , "Sandwich" , "Coke" ]
        while True:
            input_user=int(input("return(o), print(1), create(2), update(3) or delete(4): "))
            if input_user == 0:
                break
            elif input_user == 1  :
                print(products_list)
            elif input_user == 2  :
                products_list.append(input("new product: "))     
                print(products_list)
            elif input_user == 3  :
                print_list(products_list)
                products_list[int(input("the index of product: "))] = input("new product name: ")
                print(products_list)
            elif input_user == 4  :
                print_list(products_list)
                del products_list[int(input("the index of product: "))]
                print(products_list)


    elif inputt ==2:
        print(courier_menu_option)
        couriers_list=["Sara", "Sina"]
        while True:
            input_user2=int(input("return(o), print(1), create(2), update(3) or delete(4): "))
            if input_user2 == 0:
                break
            elif input_user2 == 1  :
                print(courier_menu_option)
            elif input_user2 == 2  :
                couriers_list.append(input("new courier: "))     
                print(couriers_list)
            elif input_user2 == 3  :
                print_list(couriers_list)
                couriers_list[int(input("the index of courier: "))] = input("new courier name: ")
                print(couriers_list)
            elif input_user2 == 4  :
                print_list(couriers_list)
                del couriers_list[int(input("the index of courier: "))]
                print(couriers_list)