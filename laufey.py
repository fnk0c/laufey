#!/usr/bin/python

__AUTHOR__	= "Fnkoc"
__GITHUB__	= "http://github.com/fnk0c"
__LICENSE__	= "GPLv2"

from sys import platform
from subprocess import check_output, check_call
from time import sleep

#Sleep is needed because all modules and applications need to
#be loaded before we can start the check and stuff
sleep(5)

"""---------Please edit the following variables
according to your needs"""
#Device name
#On linux the device name is retrieved using the command "lsusb"
#On Windows it's the label name of flash drive
flashDisk = "Toshiba OR use its ID 1234:5678"

"""
Linux users must change the lock command if not
using xscreensaver.
"""

if platform == "win32":
	sys = "windows"

	"""Windows"""
	#List all removable devices
	list_device = ["wmic", "logicaldisk", "get", "volumename"]

	#Lock screen
	lock = "rundll32.exe user32.dll,LockWorkStation"

	#Check if screen is locked
	#The verification is not working, but even without it the
	#script works like charm. So, it's not needed, but i'll keep
	#it on the code
	#status = "rundll32.exe User32\OpenInputDesktop\",\"int\",0*0,\"int\",0*0,\"int\",0x0001L*1"
elif platform == "linux2" or platform == "linux":
	sys = "linux"

	"""Linux"""
	#List all removable devices
	list_device = "lsusb"

	#Lock screen
	lock = ["xscreensaver-command", "-lock"]
	
	#Check if screen is locked
	status = ["xscreensaver-command", "-time"]
else:
	print("Your system is not supported!")
	exit()

"""---------End variables"""

while True:
	#Retrieve devices list and check if flashdrive is on it
	disks = check_output(list_device)

	#If not in list, checks if screen is already locked and lock if not
	if flashDisk not in str(disks):
		if sys == "linux":
			try:
				status_response = check_output(status)

				if "locked" in  status_response.decode("utf-8").split():
					print("Locked")
				else:
					check_call(lock)
			except Exception as e:
				print("An error occoured\n" + str(e))
		elif sys == "windows":
			check_call(lock)
	else:
		pass
	sleep(2)
