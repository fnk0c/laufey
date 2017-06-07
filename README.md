# Laufey
Lock user screen every time the flash drive is unplugged. Creating a two-step authentication on the machine

## How it works?
Every time you start the application, it initiates a process that is constantly verifying if the usb device is connected to the computer.

##### What if it's not connected?
If the device could not be found, the program sends a message to the system in order to lock the screen. This way, you can only use the computer if you have the **password and the flash drive**

## What are the requirements?
1. Flash drive
2. Computer running Windows or Linux (tested on Windows 7 and Arch Linux. Others distributions should work like charm)
3. Python 2 or 3 interpreter (Windows users can compile the application using py2exe)

## How to use?
* Edit the source in order to change the variables values  

Only change the device name from `flashDisk = "CHANGE_ME"` to whatever is your device serial number  

![Imgur](http://i.imgur.com/9IBWrS9.png)

**Windows users**  
The following command can be used to determinate the serial number  
1. Verify if flash drive is connected  

`wmic logicaldisk get volumename`  

![Imgur](http://i.imgur.com/XDaNiGs.png)  

2. Get its serial number  

`wmic logicaldisk get volumeserialnumber`  

![Imgur](http://i.imgur.com/G05u435.png)  

**Linux users**  
The following command can be used  

`lsusb | cut -d " " -f 6-`

![Imgur](http://i.imgur.com/awEgzSM.jpg)

Below the red thing you will find something like *a1b2:3456*. That's exactly the information you are looking for.  

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
