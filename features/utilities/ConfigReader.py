from configparser import ConfigParser


def basic_info(category, key):
    try:
        config = ConfigParser()
        config.read("features/configurations/basic_info.ini")
        return config.get(category, key)
    except:
        print("****************************File not found****************************")


def expected_outcome(category, key):
    try:
        config = ConfigParser()
        config.read("features/configurations/expected_outcome.ini")
        return config.get(category, key)
    except:
        print("****************************File not found****************************")


def login(category, key):
    try:
        config = ConfigParser()
        config.read("features/configurations/login.ini")
        return config.get(category, key)
    except:
        print("****************************File not found****************************")


def urls(category, key):
    try:
        config = ConfigParser()
        config.read("features/configurations/urls.ini")
        return config.get(category, key)
    except:
        print("****************************File not found****************************")


def create_inbound_inventory(category, key):
    try:
        config = ConfigParser()
        config.read("features/configurations/create_inbound_inventory.ini")
        return config.get(category, key)
    except:
        print("****************************File not found****************************")


def vendor_invoices_and_packing_slips(category, key):
    try:
        config = ConfigParser()
        config.read("features/configurations/vendor invoice & packing slips.ini")
        return config.get(category, key)
    except:
        print("****************************File not found****************************")
