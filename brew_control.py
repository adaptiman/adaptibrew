#!/usr/bin/env python

import omegacn7500
import str116
import settings
import sys

# Connect to the PID instrument to get status values
instr = omegacn7500.OmegaCN7500(settings.port,settings.rimsAddress)

# Connect to str116 API to check relay status
# EXAMPLSE: str116.get_relay(settings.relays['pump'])

def main_loop():
    '''Show the main menu interface and handle user instructions'''

    while True:
        show_main_menu()
        choice = input('Make a selection from the menu above: ')
        #print "You chose {}".format(choice)
        print
        if choice == 1:
            toggle_relay_menu()
        elif choice == 2:
            toggle_pump()
        elif choice == 3:
            toggle_pid()
        elif choice == 4:
            set_target_temp()
        elif choice == 5:
            select_stage()
        elif choice == 9:
            print "Goodbye!"
            sys.exit()
        else:
            print "Invalid selection. Please choose the numbers above."


def show_main_menu():
    PUMP_STATE = 'ON' if str116.get_relay(settings.relays['pump']) else 'OFF'
    PID_STATE = 'ON' if instr.is_running() else 'OFF'
    TARGET_TEMP = instr.get_setpoint()
    CURRENT_TEMP = instr.get_pv()
    print '''
Please select an option:

   1. Toggle valve relay
   2. Toggle pump (pump currently {})
   3. Toggle PID (PID currently {})
   4. Set PID target temp (currently {}; actual temp {})
   5. Set brewer stage (currently in RIMS)

   9. Exit brew controller
'''.format(PUMP_STATE, PID_STATE, TARGET_TEMP, CURRENT_TEMP)

def toggle_relay_menu():
    STATE_0 = 'ON' if str116.get_relay(settings.relays["hltToMash"]) else 'OFF'
    STATE_1 = 'ON' if str116.get_relay(settings.relays["hlt"]) else 'OFF'
    STATE_2 = 'ON' if str116.get_relay(settings.relays["rimsToMash"]) else 'OFF'
    print '''
Please select an option:

   0. Sparge-to-mash valve (currently {})
   1. Sparge valve (currently {})
   2. RIMS-to-mash valve (currently {})

   9. Return to main menu
'''.format(STATE_0, STATE_1, STATE_2)

    choice = input("Select a valve from the choices above: ")
    if choice == 9:
        return
    if isinstance(choice, int) and choice < 3:
        toggle_relay(choice)
    else:
        print "Invalid option. Please select a number from the list above."
        toggle_relay_menu()

def toggle_relay(relay_address):
    if isinstance(relay_address, int) and relay_address < 3:
        if str116.get_relay(relay_address):
            print 'Turning valve OFF . . . ',
            str116.set_relay(relay_address, 0)
        else:
            print 'Turning valve ON . . . ',
            str116.set_relay(relay_address, 1)
        print 'DONE'
    else:
        print 'INVALID RELAY ADDRESS'

def toggle_pump():
    if str116.get_relay(settings.relays['pump']):
        print 'Turning pump OFF . . . ',
        str116.set_relay(settings.relays['pump'], 0)
    else:
        print 'Turning pump ON . . . ',
        str116.set_relay(settings.relays['pump'], 1)
    print 'DONE'

def set_pump_on():
    print 'Turning pump ON . . . ',
    str116.set_relay(settings.relays['pump'], 1)
    print 'DONE'

def set_pump_off():
    print 'Turning pump OFF . . . ',
    str116.set_relay(settings.relays['pump'], 0)
    print 'DONE'

def toggle_pid():
    if instr.is_running():
        print 'Turning PID OFF . . . ',
        instr.stop()
    else:
        print 'Turning PID ON . . . ',
        instr.run()
    print 'DONE'

def set_target_temp():
    temp_val = input("Specify target temperature for PID: ")
    # need tp sanity check the input for a valid number
    instr.set_setpoint(temp_val)

def select_stage():
    print '''Specify a brew stage:
   1. RIMS stage (Recirculating Infusion Mash System)
   2. Sparge stage
   3. Boil stage

   9. Return to main menu
 '''
    stage_choice = input("Select a brew stage from the choices above: ")
    if stage_choice == 1:
        set_RIMS_stage()
    elif stage_choice == 2:
        set_sparge_stage()
    elif stage_choice == 3:
        set_boil_stage()
    elif stage_choice == 9:
        return
    else:
        print "Invalid option. Please select a number from the list above."

def detect_stage():
    pass

def set_RIMS_stage():
    # hlt OFF, rimsToMash ON, pump ON, PID ON, target temp 150
    # "Directing RIMS valve to mash tun"
    pass


def set_sparge_stage():
    # set relay 1 (hlt) to ON, wait 10 seconds
    print 'Setting sparge valve ON ',
    str116.set_relay(settings.relays['hlt'], 1)
    import time
    for i in range(1,11):
        print ',',
        time.sleep(1)
    print ' DONE'

    # set relay 2 (rimsToMash) to OFF
    print 'Directing RIMS valve to boil tun . . . ',
    str116.set_relay(settings.relays['rimsToMash'], 0)
    print 'DONE'

    # ensure that PID is ON
    if instr.is_running() == False:
        print 'Turning PID ON . . . ',
        instr.run()
        print 'DONE'
    # TODO: set temp according to calculator

def set_boil_stage():
    # pump OFF, PID OFF, hlt OFF
    pass


if __name__ == '__main__':
    main_loop()
