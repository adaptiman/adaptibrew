# adaptibrew
#####Author: David Sweeney
#####Email:  adaptiman@tamu.edu

###Overview:
Adaptibrew is a Python based toolset used to control varioius processes in my custom brewery. The toolset uses a RPiv.2 processor coupled with an RS485 shield used to control various electrical valves and process devices such as the Omega CN7500 proportional PID controller (used to control RIMS).

###License:
#####Author: David Sweeney
#####Email:  adaptiman@tamu.edu
adaptibrew is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International license [Copy Found Here](http://creativecommons.org/licenses/by-nc-sa/4.0/)

###Users/Audience:
 * Homebrewers
 * Programers
 * Tinkerers

This project is aimed at any tech savvy individuals who want to get into home brewing or are looking for help to automate their home brewing process. 

###Components Used:
 * [5- Pack WaterProof Temperature Sensors](http://www.amazon.com/gp/product/B00EU70ZL8/ref=oh_aui_detailpage_o02_s00?ie=UTF8&psc=1)
 

###Setup:
The newer raspian images do not have the correct settings in the config. You must add the following line to your boot config if it is not present.
```shell
dtoverlay=w1-gpio
```

You will also have to install WiringPi library. The library is at the bottom but here is a direct link to the install instructions. [HERE](http://wiringpi.com/download-and-install/)

###Running:
Simply run the following through a terminal or ssh.
```shell
sudo ./adaptibrew
```

###Prior Work and Libraries:
 * [WiringPi](http://wiringpi.com) - Raspberry Pi GPIO library for C

###Demonstration
[Demonstration Video](https://youtu.be/usqvsCGNW-Y)