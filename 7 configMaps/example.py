import os

for i in range(100):
    config_value = os.environ.get("CONFIG_VALUE", "default_value")
    print("Config Value:", config_value)
