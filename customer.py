from apps import AppStore


class Customer:
    """
    A class to represent a customer

    Attributes
    ----------
    cart : list
        a list to add an app in cart
    total : float
        store total price of apps in the cart
    

    Methods
    -------
    add_to_cart(app_name)
        add an app to cart
    
    delete_from_cart(app_name)
        delete an app from cart
    
    checkout()
        display the list of apps in the cart and their total price
    """

    def __init__(self):
        self.cart = []
        self.total = float(0)

    def __show_cart(self):
        print("*"*11+"Your Cart"+"*"*11+"\n")
        print("Name--price")
        for i in range(len(self.cart)):
            print(self.cart[i])
        print("\n")

    def add_to_cart(self, app_name):
        for i in range(len(AppStore.app_list)):
            app, price = AppStore.app_list[i].split(':')
            if str.lower(app) == str.lower(app_name):
                self.cart.append("{}--{}".format(app, price))
                self.total += float(price[1:])
                print("{} is added to cart\n".format(app))
                self.__show_cart()
                return
        print("no such item available in app store")
    
    def delete_from_cart(self, app_name):
        for i in range(len(self.cart)):
            app, price = self.cart[i].split('--')
            if str.lower(app) == str.lower(app_name):
                self.total -= float(price[1:])
                self.cart.pop(i)
                print("{} is deleted from cart".format(app))
                self.__show_cart()
                return
        print("no such item is in your cart")
        self.__show_cart()
                
    
    def checkout(self):
        print("\nYour cart:")
        for i in range(len(self.cart)):
            app, price = self.cart[i].split('--')
            print("{}--{}".format(app, price[1:]))
        print("Your Total: {:.2f}\n".format(self.total))

        

