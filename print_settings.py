import settings, sys, json

master_settings_dict = {}
# get all the settings names, exluding those returned by dir()
# i. e. __doc__, __name__
# If it includes "__", then remove it
list_of_setting_names = [x for x in dir(settings) if not "__" in x]

# For all the settings names
for setting in list_of_setting_names:
    # get the value of that setting and add it to master_settings_dict
    master_settings_dict[setting] = getattr(settings, setting)

json.dump(master_settings_dict, sys.stdout)
