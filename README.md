# VRControlPanel
 Virtual rover control panel created for team diana code challenge.
 Powered by python3.9 and PyQt5!

### Control panel
![image](https://github.com/marcobackup/VRControlPanel/blob/main/docs/main%20window.png?raw=true)

### How to start
- Install python3.9, pipenv and initialize virtual environment in main root (VRControlPanel/)
> pip install pipenv

> pipenv shell
- Install software dependencies
> pip install -r requirements.txt
- Start the VR control panel
> python -m vrcontrolpanel

Please note, if clicking on publish the values aren't updated, restart Recruitment_VirtualRover.exe which doesn't update the values on the topics `VR/rover/feedback/velocity` and `VR/rover/feedback/steeringAngle`.
