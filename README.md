# VENT

VENT or Visualization for Evil Network Traffic is a local web application built on Django that will allow network administrators to quickly view the status of their network and take action on any malicious activity they identify.

VENT will start by building a visualization of your network topology by passively listening in on the network's traffic. Then an intrusion detection system, Bro, will analyze the network for evil or malicious traffic. As it detects malicious traffic, the machine's color on the visualization of the network will turn from green to red. This will allow network administrators to determine the status of their network and if anything is being attacked at a quick glance.

Once the network administrator identifies malicious traffic, they can then choose to act on this traffic by performing network administrative actions such as black-holing, reconnaissance, and port scanning.

To get up and running:

1. Download the project
2. Install Django
3. Run 'python manage.py runserver'
4. Navigate to localhost:8000/topology/
5. ??????
6. Profit

# Future Work
1. Add support to allow you to add multiple subnets and be able to navigate to different ones with ease.
2. Add blackhole feature so you can quickly blackhole malicious hosts
3. Add machine naming so you can identify what resources are being utilized on that server
4. See a list of the top 5 attacker when you click on a machine
5. Add filtering to machines and attacker so you can look for IPs, attacks, or dates
6. Make a report commenting on the status of the network as a hole
7. Add cool visualizations to machine, attacker, and index pages to represent attacks
8. Overall prettier UI
9. Make machines draggable with click of button so you can make meaningful placements
10. Set configurations to define threat levels instead of hardcoded values.
