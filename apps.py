
class AppStore():
    """
    A class to represent an App store
    
    Attributes
    ----------
    app_list : list
        a list to store apps available in app store with its price seperated by :
    
    Methods
    -------
    display_all_apps()
        display all the apps in the app store with its price
    
    """

    app_list = [
        'weather channel:$1.99',
        'Bubble Shooter:$0.99',
        'Gallery Pro:$1.09',
        'Scanner Pro:$2.99',
        'Voice Recorder:$3.99',
        'Peak Finder:$4.99'
    ]

    @staticmethod
    def display_all_apps():
        print("*"*11 + " List of apps " + "*"*11)
        print("\nName--price")
        print("-"*25)
        for i in range(len(AppStore.app_list)):
            app, price = AppStore.app_list[i].split(':')
            print("{}--{}".format(app, price))




