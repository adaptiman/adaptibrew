#!/usr/bin/env python

# PowerOn
# 	turn PID off
# 	turn pump off
# 	turn RIMS relay ON
# 	display status of all relays
#   display status of RIMS

import set_pid_off
import str116
import click

@click.command()
def startup():
    try:
        set_pid_off()
        click.echo("PID is OFF")
    except:
        click.echo("PID is ON")

if __name__ == '__main__':
    startup()
