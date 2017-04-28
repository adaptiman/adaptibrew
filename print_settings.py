import settings

master_settings_dict = {}
# get all the settings names, exluding those returned by dir()
# i. e. __doc__, __name__
# If it includes "__", then remove it
list_of_settings = [x for x in dir(settings) if not "__" in x]

# For all the settings names
for setting in list_of_settings:
    # get the value of that setting and add it to master_settings_dict
    master_settings_dict[setting] = getattr(settings, setting)

# Print all the settings to be parsed by ruby from llamicron/brewer
for setting_key, setting_value in master_settings_dict.items():
    if setting_key == "relays":
        for relay_key, relay_address in setting_value.items():
            print relay_key, " = ", relay_address
    else:
        print setting_key, " = ", setting_value
