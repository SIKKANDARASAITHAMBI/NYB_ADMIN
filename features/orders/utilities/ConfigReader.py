from configparser import ConfigParser


def basic_info(category, key):
    try:
        config = ConfigParser()
        config.read("features/orders/configurations/basic_info.ini")
        return config.get(category, key)
    except:
        print("****************************File not found****************************")

def login(category, key):
    try:
        config = ConfigParser()
        config.read("features/orders/configurations/login.ini")
        return config.get(category, key)
    except:
        print(Exception)
        print("****************************File not found****************************")


def urls(category, key):
    try:
        config = ConfigParser()
        config.read("features/orders/configurations/urls.ini")
        return config.get(category, key)
    except:
        print(Exception)
        print("****************************File not found****************************")

def create_order(category, key):
    try:
        config = ConfigParser()
        config.read("features/orders/configurations/create_order.ini")
        return config.get(category, key)
    except:
        print(Exception)
        print("****************************File not found****************************")

