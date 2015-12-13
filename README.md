# laufey
Lock user screen every time the flash drive is unplugged. Creating a two-step authentication on the machine

##How it works?
Every time you start the application, it initiates a process that is constantly verifying if the usb device is connected to the computer.

#####What if it's not connected?
If the device could not be found, the program sends a message to the system in order to lock the screen. This way, you can only use the computer if you have the password and the flash drive

##What are the requirements?
1. Flash drive
2. Computer running Windows or Linux (tested on Windows 7 and Arch Linux. Others distributions should work like charm)
3. Python interpreter (Windows users can compile the application using py2exe)

##How to use?
* Edit the source in order to change the variables values  

**Windows users**  
Only change the device name from `flashDisk = "Toshiba"` to whatever your device is called  

**Linux users**  
Change the device name from `flashDisk = "Toshiba"` using `lsusb` to get the correct name  

The following command can be used  
`$ lsusb | cut -d " " -f 7-`

***If not using Xscreensaver***, please edit the following lines  
```
49	#Lock screen
50	lock = ["xscreensaver-command", "-lock"]
51	
52	#Check if screen is locked
53	status = ["xscreensaver-command", "-time"]
```
* type `python laufey.py` and it's done  

##License
This program is distribuited under GPLv2 license. For more informations, read LICENSE
