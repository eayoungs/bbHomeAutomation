bbHomeAutomation
================
##WARNING##
This is the very very beginning of a project. I am unsure if this code works on the BeagleBone. (awaiting its arrival). Most features aren't yet implemented, but it has been working on a prior prototype build using an ARM processor and Arduinos for I/O.
With that being said, Here's the good stuff:


##GOOD STUFF##
A Flexible / Dynamic home Automation System built with Django, Python and a BeagleBone

This started off as a project to automate my two-story shed / ManCave. Now, I saw something nice here, that didn't exist in other 'one-size-fits-all' solutions. I want this to be simple, yet as powerful as the commercially available solutions. This is aimed at the DIY-ER.

This is just the start of a big project. 

Current Features:
*   JqueryMobile UI
*   PushButton Switches for lights
*   Sensors
*   Online Control
*   User Accounts with Permissions on a per-control basis (deny users access to certain lights & features, etc;)



Planned Features:
*   AJAX online UI, mobile app support
*   More customization, more intuitave
*   Support for X10
*   Support for reading sensors, switches, more over the network, from an Arduino with Ethernet Shield
*   Security System
*   Heating / Air Conditioning
*   Options for Electronic Door Locks
*   Install & Go. No configuration necessary.
*   Support for LCD pads (arduino) with keypad. (Over Network)
*   Support for Touch Screen Controllers (Over Network)
*   Music Management
*   Support for Raspberry Pi
*   Support for manual Commands over Web Interface
*   Simple & Easy Administration
*   Options for a central system, or a distributed system with main processor. This way, each room can have its own processor that controlls lights & features for that room, but is able to interface and update statusses on main system. 
*   Ability to add boards & controls from web interface.
Right now, its 90% run from Django. I plan on utilizing two seperate 'programs' to make one system. The Hardware will be all in one system, with APIs that interact with the online django webapp, and with the hardware sensor/button loop
