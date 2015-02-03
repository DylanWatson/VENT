# VENT

VENT or Visualization for Evil Network Traffic is a local web application built on Django that will allow network administrators to quickly view the status of their network and take action on any malicious activity they identify.

VENT will start by building a visualization of your network topology by passively listening in on the network's traffic. Then an intrusion detection system, Bro, will analyze the network for evil or malicious traffic. As it detects malicious traffic, the machine's color on the visualization of the network will turn from green to red. This will allow network administrators to determine the status of their network and if anything is being attacked at a quick glance.

Once the network administrator identifies malicious traffic, they can then choose to act on this traffic by performing network administrative actions such as black-holing, reconnaissance, and port scanning.

To get up and running:

1. Download the project
2. Install Django
3. Run 'python manage.py startserver'
4. Navigate to localhost:8000/topology/
5. ?
6. Profit
