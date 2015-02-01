# VENT

VENT or Visualization for Evil Network Traffic is web application that will allow network administrators to quickly view the status of their network and take action on any malicious activity they identify.

VENT will start by building a visualization of your network topology by passively listening in on the network's traffic. Then an intrusion detection system, Bro, will analyze the network for evil or malicious traffic. As it detects malicious traffic, the machine's color on the visualization of the network will turn from green to red. This will allow network administrators to determine the status of their network and if anything is being attacked at a quick glance.

Once the network administrator identifies malicious traffic, they can then choose to act on this traffic by performing network administrative actions such as black-holing, reconnaissance, and port scanning. 
