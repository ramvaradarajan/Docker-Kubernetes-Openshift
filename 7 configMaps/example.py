import os

config_value = os.environ.get("CONFIG_VALUE", "default_value")
print("Config Value:", config_value)
