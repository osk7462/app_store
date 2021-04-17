from apps import AppStore
from customer import Customer

if __name__ == '__main__':
    print("*"*11 + "Welcome to mini app store " + "*"*11)
    options = " 1:Display apps\n 2:Add apps to my cart\n 3:Delete an apps from cart\n 4:Checkout\n 5:Exit\n\n"
    customer = Customer()
    while(True):
        print("\nAvailable options:\n{}".format(options))
        option = input("Enter option: ")
        if option == '1':
            AppStore.display_all_apps()
        elif option == '2':
            app_name = input("Enter app name to add to cart: ")
            customer.add_to_cart(app_name)
        elif option == '3':
            app_name = input("Enter app name to delete from cart: ")
            customer.delete_from_cart(app_name)
        elif option == '4':
            customer.checkout()
        elif option == '5':
            print("*"*11 + " Thanks for shopping with us " + "*"*11)
            break
        else:
            print("please choose a valid option")
        print("*"*25)
        

        
