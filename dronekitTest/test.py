print ("Start simulator (SITL)")
import dronekit_sitl

#change this if using standalone (not running using the map view)
STANDALONE = False

sitl = dronekit_sitl.start_default()
if(STANDALONE):
    connection_string = sitl.connection_string()
else:
    #hardcode value for a custom build SITL instance (what we have)
    connection_string = "udp:127.0.0.1:14550"

'''
***NOTE***
YOU MUST ADD AN OUTPUT IN ORDER FOR THIS TO WORK VIA MAVPROXY
via 
output add 127.0.0.1:14550

'''


#apparently python3 ver 10 broke a ton of libraries, so i got this from stack overflow
import sys

if sys.version_info.major == 3 and sys.version_info.minor >= 10:
    import collections
    setattr(collections, "MutableMapping", collections.abc.MutableMapping)




# Import DroneKit-Python

from dronekit import connect, VehicleMode, LocationGlobal, LocationGlobalRelative
from pymavlink import mavutil # Needed for command message definitions
import time
import math




# Connect to the Vehicle.
print("Connecting to vehicle on: %s" % (connection_string,))
vehicle = connect(connection_string, wait_ready=True)

# Get some vehicle attributes this acts as a hello world of sorts
print ("Get some vehicle attribute values:")
print (" GPS: %s" % vehicle.gps_0)
print (" Battery: %s" % vehicle.battery)
print (" Last Heartbeat: %s" % vehicle.last_heartbeat)
print (" Is Armable?: %s" % vehicle.is_armable)
print (" System status: %s" % vehicle.system_status.state)
print (" Mode: %s" % vehicle.mode.name)



#BEGIN MOVEMENT PART
vehicle.mode = VehicleMode("GUIDED")
a_location = LocationGlobalRelative(33.48559092968529, -81.97467282453941, 30)#just above the KSFO airport terminal
vehicle.simple_goto(a_location)



# Close vehicle object before exiting script
vehicle.close()

# Shut down simulator
if(STANDALONE):
    sitl.stop() #only use this if you are not running the map/simulator view. Crashes otherwise.
print("Completed")