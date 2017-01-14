#!/usr/bin/env python

import omegacn7500
import str116
import settings

# Connect to the PID instrument to get status values
instr = omegacn7500.OmegaCN7500(settings.port,settings.rimsaddressint)

# Connect to str116 API to check relay status
# EXAMPLSE: str116.get_relay(settings.pumpRelay)

def main_loop():
    '''Show the main menu interface and handle user instructions'''

    while True:
        show_main_menu()
        choice = input('Make a selection from the menu above: ')
        #print "You chose {}".format(choice)
        print
        if choice == 1:
            print "TODO: SHOW SOME STATUS"
        elif choice == 2:
            toggle_pump()
        elif choice == 3:
            toggle_pid()
        elif choice == 4:
            set_target_temp()
        elif choice == 5:
            select_stage()
        else:
            print "Invalid selection. Please choose the numbers above."


def show_main_menu():
    PUMP_STATE = 'ON' if str116.get_relay(settings.pumpRelay) else 'OFF'
    PID_STATE = 'ON' if instr.is_running() else 'OFF'
    TARGET_TEMP = instr.get_setpoint()
    CURRENT_TEMP = instr.get_pv()
    print '''
Please select an option:

   1. Show status info
   2. Toggle pump (pump currently {})
   3. Toggle PID (PID currently {})
   4. Set PID target temp (currently {}; actual temp {})
   5. Set brewer stage (currently in RIMS)
'''.format(PUMP_STATE, PID_STATE, TARGET_TEMP, CURRENT_TEMP)

def toggle_pump():
    if str116.get_relay(settings.pumpRelay):
        print 'Turning pump OFF . . . ',
        str116.set_relay(settings.pumpRelay, 0)
    else:
        print 'Turning pump ON . . . ',
        str116.set_relay(settings.pumpRelay, 1)
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
 '''
    stage_choice = input("Select a brew stage from the choices above: ")
    if stage_choice == 1:
        set_RIMS_stage()
    elif stage_choice == 2:
        set_sparge_stage()
    elif stage_choice == 3:
        set_boil_stage()
    else:
        print "Invalid option. Please select a number from the list above."

def detect_stage():
    pass

def set_RIMS_stage():
    # spargeRelay OFF, rimsToMashRelay ON, pump ON, PID ON, target temp 150
    # "Directing RIMS valve to mash tun"
    pass


def set_sparge_stage():
    # set relay 1 (spargeRelay) to ON, wait 10 seconds
    print 'Setting sparge valve ON ',
    str116.set_relay(settings.spargeRelay, 1)
    import time
    for i in range(1,11):
        print ',',
        time.sleep(1)
    print ' DONE'

    # set relay 2 (rimsToMashRelay) to OFF
    print 'Directing RIMS valve to boil tun . . . ',
    str116.set_relay(settings.rimsToMashRelay, 0)
    print 'DONE'

    # ensure that PID is ON
    if instr.is_running() == False:
        print 'Turning PID ON . . . ',
        instr.run()
        print 'DONE'
    # TODO: set temp according to calculator

def set_boil_stage():
    # pump OFF, PID OFF, spargeRelay OFF
    pass


if __name__ == '__main__':
    main_loop()
