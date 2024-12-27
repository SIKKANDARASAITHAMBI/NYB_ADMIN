from configparser import ConfigParser


def basic_info(category, key):
    try:
        config = ConfigParser()
        config.read("features/orders/configurations/create_order.ini")
        return config.get(category, key)
    except:
        print("****************************File not found****************************")
