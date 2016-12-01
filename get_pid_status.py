#!/usr/bin/env python
import minimalmodbus
import omegacn7500
import settings

instr = omegacn7500.OmegaCN7500(settings.port,settings.rimsaddressint)
# port name, slave address

minimalmodbus._print_out( 'Control:                {0}'.format(  instr.get_control_mode()    ))
minimalmodbus._print_out( 'SP:                     {0}'.format(  instr.get_setpoint() ))
minimalmodbus._print_out( 'PV:                     {0}'.format(  instr.get_pv()       ))
minimalmodbus._print_out( 'OP1:                    {0}'.format(  instr.get_output1()  ))
minimalmodbus._print_out( 'Is running:             {0}'.format(  instr.is_running()   ))
minimalmodbus._print_out( 'Start pattern:          {0}'.format(  instr.get_start_pattern_no()  ))
minimalmodbus._print_out('DONE!')
