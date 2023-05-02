# HotWater
HotWater monitoring 

## To Develop
Open the "Ubuntu 18.0.3 LTS" VM to host the Jenkins build server

At a DOS promp type wsl to bring up a Lunux promp

In Pycharm pushing to Jenkins should initiate a Jenkins build via the hooks.
If it doesn't work it's because the external IP of my router has changed
so change it in:
https://github.com/andye456/HotWater/settings/hooks/396618351?tab=deliveries

Once updated test by "redelivering"

Open Mobs and use AWS